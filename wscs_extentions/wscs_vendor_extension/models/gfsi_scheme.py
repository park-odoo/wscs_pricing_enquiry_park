# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class gfsiScheme(models.Model):
    _name = 'gfsi.scheme'
    _description = 'GFSI Scheme'

    name = fields.Char(string="Scheme")
