# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class PriceEnquiryOrderLine(models.Model):
    _name = 'price.enquiry.order.line'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'product.catalog.mixin'] 
    _description = 'Price Enquiry Order Line'

    # FIELDS DECLARATION
    name = fields.Char(string='Description')
    product_id = fields.Many2one(comodel_name='product.product', string='Product')
    customer_code = fields.Char(string='Customer Code')
    categ_id = fields.Many2one(comodel_name='product.category', related='product_id.categ_id', string='Product Category')
    est_volume = fields.Float(string='Estimated Volume')
    product_uom_id = fields.Many2one(comodel_name='uom.uom', string='UOM')
    height  = fields.Float(string='Height')
    width = fields.Float(string='Width')
    depth = fields.Float(string='Depth')
    diameter = fields.Float(string='Diameter')
    material = fields.Char(string='Material')
    price_enquiry_id = fields.Many2one(comodel_name='price.enquiry', string='Price enquiry')
    company_id = fields.Many2one(comodel_name='res.company', related='price_enquiry_id.company_id')
    display_type = fields.Selection([('line_section', "Section"), ('line_note', "Note")], default=False)

    def action_add_from_catalog(self):
        order = self.env['price.enquiry'].browse(self.env.context.get('order_id'))
        return order.action_add_from_catalog()
