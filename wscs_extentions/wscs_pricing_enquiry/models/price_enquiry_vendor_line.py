# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class PriceEnquiryVendorLine(models.Model):
    _name = 'price.enquiry.vendor.line'
    _description = 'Price Enquiry Vendor Line'

    # FIELDS DECLARATION
    partner_id = fields.Many2one(comodel_name='res.partner', string='Vendor', domain="[('supplier_rank','>',0)]")
    price_enquiry_id = fields.Many2one(comodel_name='price.enquiry', string='Price enquiry')

    def action_send_email(self):
        pass

    def action_re_send_email(self):
        pass

    def action_send_reminder(self):
        pass
