# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class SupplierInfo(models.Model):
    _inherit = "product.supplierinfo"

    qty_per_case = fields.Integer(string='Quantity per case')
    cases_per_container = fields.Integer(string='Cases per Container')
    price_per_1000 = fields.Float(string='Cost per 1000')
    incoterm_id = fields.Many2one('account.incoterms', string='Incoterms')