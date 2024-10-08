# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api
from odoo.exceptions import ValidationError


class ProductPalletspec(models.Model):
    _name = 'product.palletspec'
    _description = 'Product Pallet Specification'

    # FIELDS DECLARATION
    name = fields.Char(string='Pallet Type')
    product_template_id = fields.Many2one(required=True, comodel_name='product.template', string='Product')
    cases_per_layer = fields.Float(required=True, string='Cases per Layer')
    layers_per_pallet = fields.Float(required=True, string='Layers per Pallet')
    qty = fields.Float(required=True, compute='qty_compute_field', string='Contained Quantity')
    product_uom_id = fields.Many2one(comodel_name='uom.uom', string='Unit of Measure')
    width = fields.Integer(required=True, string='Width')
    length = fields.Integer(required=True, string='Length')
    height = fields.Integer(required=True, string='Height')
    volume = fields.Float(compute='volume_compute_field', digits=(16, 4), string='Volume (m³)')
    weight = fields.Float(string='Weight')
    units = fields.Integer(compute='units_compute_field', string='Pieces per Pallet')

    _sql_constraints = [
        ('check_cases_per_layer', 'CHECK(cases_per_layer>0.0)', 'Cases per Layer should have value.'),
        ('check_layers_per_pallet', 'CHECK(layers_per_pallet>0.0)', 'Layers per Pallet should have value.'),
        ('check_width', 'CHECK(width>0)', 'Width should have value.'),
        ('check_length', 'CHECK(length>0)', 'Length should have value.'),
        ('check_height', 'CHECK(height>0)', 'Height should have value.'),
    ]

    @api.depends('cases_per_layer', 'layers_per_pallet')
    def qty_compute_field(self):
        for rec in self:
            qty = rec.cases_per_layer * rec.layers_per_pallet
            if qty and len(str(int(qty))) > 3:
                raise ValidationError("Contained Quantity cannot exceed 3 digits.")
            else:
                rec.qty = qty

    @api.depends('cases_per_layer', 'layers_per_pallet', 'product_template_id')
    def units_compute_field(self):
        for rec in self:
            rec.units = (rec.cases_per_layer * rec.layers_per_pallet) * sum(packaging.qty for packaging in rec.product_template_id.packaging_ids)

    @api.depends('width', 'length', 'height')
    def volume_compute_field(self):
        for rec in self:
            volume = (rec.width * rec.length * rec.height) / 1000000000
            if volume and len(str(int(volume))) > 4:
                raise ValidationError("Volume cannot exceed 4 digits.")
            else:
                rec.volume = volume
