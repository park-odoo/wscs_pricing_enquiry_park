# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api, _
from collections import defaultdict
from dateutil.relativedelta import relativedelta


class PriceEnquiry(models.Model):
    _name = 'price.enquiry'
    _inherit = ['product.catalog.mixin', 'mail.thread', 'mail.activity.mixin']
    _description = 'price Enquiry'

    # FIELDS DECLARATION
    name = fields.Char(string='Number', default='New')
    partner_id = fields.Many2one(comodel_name='res.partner', string='Customer')
    expiration_date = fields.Date(string='Expiration')
    enquiry_date = fields.Datetime(string='Enquiry Date')
    state = fields.Selection([('draft', 'Enquiry'), ('sent', 'Vendor Sent'), ('quotation sent', 'Sales Quotation')], default='draft')
    enquiry_status_id = fields.Many2one(comodel_name='enquiry.status', string='Status')
    description = fields.Html(string='Description')
    price_enquiry_order_line_ids = fields.One2many(comodel_name='price.enquiry.order.line', inverse_name='price_enquiry_id', string='Price Enquiry Order Line')
    company_id = fields.Many2one(comodel_name='res.company', required=True, index=True, default=lambda self: self.env.company)
    price_enquiry_vendor_line_ids = fields.One2many(comodel_name='price.enquiry.vendor.line', inverse_name='price_enquiry_id', string='Price Enquiry Vendor Line')

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', _("New")) == _("New"):
                vals['name'] = self.env['ir.sequence'].next_by_code('price.enquiry')
        return super().create(vals_list)

    def _get_product_catalog_record_lines(self, product_ids):
        grouped_lines = defaultdict(lambda: self.env['price.enquiry.order.line'])
        for line in self.price_enquiry_order_line_ids:
            if line.display_type or line.product_id.id not in product_ids:
                continue
            grouped_lines[line.product_id] |= line
        return grouped_lines

    def action_print_price_enquiry(self):
        pass

    def action_create_sale_quotation(self):
        pass

    def action_cancel(self):
        pass

    # working----------->
    # def _track_subtype(self, init_values):
    #     breakpoint()
    #     self.ensure_one()
    #     if 'state' in init_values and self.state == 'sent':
    #         return self.env.ref('wscs_pricing_enquiry.mt_rfp_sent')
    #     return super(PricingEnquiry, self)._track_subtype(init_values)

    @api.model
    def retrieve_dashboard(self):
        """ This function returns the values to populate the custom dashboard in
            the purchase order views.
        """
        self.check_access_rights('read')

        result = {
            'all_to_send': 0,
            'all_waiting': 0,
            'all_late': 0,
            'my_to_send': 0,
            'my_waiting': 0,
            'my_late': 0,
            'all_avg_order_value': 0,
            'all_avg_days_to_purchase': 0,
            'all_total_last_7_days': 0,
            'all_sent_rfps': 0,
            'company_currency_symbol': self.env.company.currency_id.symbol
        }

        one_week_ago = fields.Datetime.to_string(fields.Datetime.now() - relativedelta(days=7))

        query = """SELECT COUNT(1)
                   FROM mail_message m
                   JOIN price_enquiry pe ON (pe.id = m.res_id)
                   WHERE m.create_date >= %s
                     AND m.model = 'price.enquiry'
                     AND m.message_type = 'notification'
                     AND m.subtype_id = %s
                     AND pe.company_id = %s;
                """

        self.env.cr.execute(query, (one_week_ago, self.env.ref('wscs_pricing_enquiry.mt_rfp_sent').id, self.env.company.id))
        res = self.env.cr.fetchone()
        result['all_sent_rfps'] = res[0] or 0
        pe = self.env['price.enquiry']
        result['all_to_send'] = pe.search_count([('state', '=', 'draft')])
        result['my_to_send'] = pe.search_count([('state', '=', 'draft'), ('partner_id.user_id', '=', self.env.uid)])
        result['all_waiting'] = pe.search_count([('state', '=', 'sent'), ('expiration_date', '>=', fields.Datetime.now())])
        result['my_waiting'] = pe.search_count([('state', '=', 'sent'), ('expiration_date', '>=', fields.Datetime.now()), ('partner_id.user_id', '=', self.env.uid)])
        result['all_late'] = pe.search_count([('state', 'in', ['draft', 'sent', 'to approve']), ('expiration_date', '<', fields.Datetime.now())])
        result['my_late'] = pe.search_count([('state', 'in', ['draft', 'sent', 'to approve']), ('expiration_date', '<', fields.Datetime.now()), ('partner_id.user_id', '=', self.env.uid)])

        return result
