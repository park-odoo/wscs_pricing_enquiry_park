# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class gfsiGrade(models.Model):
    _name = 'gfsi.grade'
    _description = 'GFSI Grade'

    name = fields.Char(string="Grade")
