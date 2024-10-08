# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class ProductStatus(models.Model):
    _name = 'product.status'
    _description = 'Product Status'

    # FIELDS DECLARATION
    name = fields.Char(string='Product Status')
    sequence = fields.Integer(string='Sequence')
    status_change_up_group_id = fields.Many2one(comodel_name='res.groups', string='Group Name - Status Change Up')
    status_change_down_group_id = fields.Many2one(comodel_name='res.groups', string='Group Name - Status Change Down')
