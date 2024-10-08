# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class Certification(models.Model):
    _name = 'certification'
    _description = 'certification'

    name = fields.Char(string="Certificate Name")
