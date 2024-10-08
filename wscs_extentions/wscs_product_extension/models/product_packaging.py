# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api
from odoo.exceptions import ValidationError


class ProductPackaging(models.Model):
    _inherit = 'product.packaging'

    # FIELDS DECLARATION
    width = fields.Integer(required=True, string='Width')
    length = fields.Integer(required=True, string='Length')
    height = fields.Integer(required=True, string='Height')
    volume = fields.Float(compute='volume_compute_field', digits=(16, 4), string='Volume (m³)')
    net_weight = fields.Float(required=True, string='Nett Weight')
    gross_weight = fields.Float(required=True, string='Gross Weight')

    _sql_constraints = [
        ('check_positive_width', 'CHECK(width>0)', 'Width should have value.'),
        ('check_positive_length', 'CHECK(length>0)', 'Length should have value.'),
        ('check_positive_height', 'CHECK(height>0)', 'Height should have value.'),
        ('check_positive_net_weight', 'CHECK(net_weight>0.0)', 'Nett Weight should have value.'),
        ('check_positive_gross_weight', 'CHECK(gross_weight>0.0)', 'Gross Weight should have value.'),
    ]

    # Constraints for length validation
    @api.constrains('width', 'length', 'height', 'volume', 'net_weight', 'gross_weight')
    def _check_digit_length(self):
        for rec in self:
            if rec.width and len(str(abs(rec.width))) > 4:
                raise ValidationError("Width cannot exceed 4 digits.")

            if rec.length and len(str(abs(rec.length))) > 4:
                raise ValidationError("Length cannot exceed 4 digits.")

            if rec.height and len(str(abs(rec.height))) > 4:
                raise ValidationError("Height cannot exceed 4 digits.")

            if rec.net_weight and len(str(int(rec.net_weight))) > 4:
                raise ValidationError("Net Weight cannot exceed 4 digits.")

            if rec.gross_weight and len(str(int(rec.gross_weight))) > 4:
                raise ValidationError("Gross Weight cannot exceed 4 digits.")

    @api.depends('width', 'length', 'height')
    def volume_compute_field(self):
        for rec in self:
            volume = (rec.width * rec.length * rec.height) / 1000000000
            if volume and len(str(int(volume))) > 4:
                raise ValidationError("Volume cannot exceed 4 digits.")
            else:
                rec.volume = volume
