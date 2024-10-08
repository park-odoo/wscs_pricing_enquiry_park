# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class EnquiryStatus(models.Model):
    _name = 'enquiry.status'
    _description = 'Enquiry Status'

    # FIELDS DECLARATION
    name = fields.Char(string='Status', default='Preparation')
    active_status = fields.Selection(selection=[('yes','Yes'),('no','No')], string='Active', default='no')
