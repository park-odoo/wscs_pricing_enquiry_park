# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api, _
from odoo.exceptions import AccessError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    BOOLEAN_SELECTION_CHOICES = [
        ('yes','Yes'),
        ('no','No'),
        ('unverified','Unverified'),
    ]
    vendor_status_id = fields.Many2one('vendor.status', string='Status')
    product_category_ids = fields.Many2many('product.category', string="Categories")
    is_sedex_registered = fields.Selection(selection=BOOLEAN_SELECTION_CHOICES, default='unverified', string='Sedex Registered')
    is_ethical_audit = fields.Selection(selection=BOOLEAN_SELECTION_CHOICES, default='unverified', string="Ethical Audit Conducted")
    is_gfsi_certification = fields.Selection(selection=BOOLEAN_SELECTION_CHOICES, default='unverified', string="GFSI Certification")
    is_fsc_certified = fields.Selection(selection=BOOLEAN_SELECTION_CHOICES, default='unverified', string="FSC Certified")
    is_pefc_certified = fields.Selection(selection=BOOLEAN_SELECTION_CHOICES, default='unverified', string="PEFC Certified")
    other_certification_id = fields.Many2one('certification', string="Other Certification")
    sedex_member_no = fields.Char(string="Sedex Member No.")
    gfsi_scheme_id = fields.Many2one('gfsi.scheme', string="GFSI Scheme")
    gfsi_grade_id = fields.Many2one('gfsi.grade', string="GFSI Grade")

    @api.constrains('vendor_status_id')
    def check_vendor_status_id(self):
        for record in self:
            users = record.vendor_status_id.status_change_user_ids
            if self.env.user not in users and users:
                raise AccessError(_('Only these user can change vendor status (%(user_name)s).',
                                    user_name = ', '.join(users.mapped('name'))),
                                )
