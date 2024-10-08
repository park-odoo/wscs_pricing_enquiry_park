# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api


class ProductTemplate(models.Model):
    _inherit = "product.template"

    # FIELDS DECLARATION
    product_status_id = fields.Many2one(comodel_name='product.status', string='Product Status', domain="[('id', 'in', suitable_product_status_ids)]")
    suitable_product_status_ids = fields.Many2many(comodel_name='product.status', compute='_compute_suitable_product_status_ids', string='Suitable Product Status')
    customer_product_code = fields.Char(string='Customer Reference', size=12)
    product_palletspec_ids = fields.One2many(comodel_name='product.palletspec', inverse_name='product_template_id', string='Product Palletspec')
    landed_cost = fields.Float(string='Landed Cost')
    margin = fields.Float(compute='margin_compute_field', string='Margin')

    @api.depends('list_price', 'standard_price', 'landed_cost')
    def margin_compute_field(self):
        for rec in self:
            rec.margin = ((rec.list_price - (rec.standard_price + rec.landed_cost)) / rec.list_price) * 100

    def _prepare_status_ids(self, domain, func_min=False, func_max=False):
        status_ids = []
        product_status_ids = self.env['product.status'].search(domain)
        if product_status_ids and func_min:
            sequence = min(product_status_ids.mapped('sequence'))
        elif product_status_ids and func_max:
            sequence = max(product_status_ids.mapped('sequence'))
        else:
            sequence = False

        for status_id in product_status_ids.filtered(lambda l: l.sequence == sequence):
            if status_id.status_change_up_group_id in self.env.user.groups_id:
                status_ids.append(status_id.id)
        return status_ids

    @api.depends('name')
    def _compute_suitable_product_status_ids(self):
        for rec in self:
            suitable_status_ids = []
            if rec.product_status_id:
                suitable_status_ids = self._prepare_status_ids([('sequence', '>', rec.product_status_id.sequence)], func_min=True)

                # Status Change Down Group is exist
                if rec.product_status_id.status_change_down_group_id in self.env.user.groups_id:
                    suitable_status_ids.extend(self._prepare_status_ids([('sequence', '<', rec.product_status_id.sequence)], func_max=True))
            else:
                suitable_status_ids = self._prepare_status_ids([], func_min=True)
            rec.suitable_product_status_ids = [(6, 0, suitable_status_ids)] if suitable_status_ids else False
