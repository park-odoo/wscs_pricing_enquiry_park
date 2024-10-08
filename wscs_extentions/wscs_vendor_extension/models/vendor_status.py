# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models,api


class VendorStatus(models.Model):
    _name = 'vendor.status'
    _rec_name = 'code'
    _description = 'Vendor Status'

    sequence = fields.Integer(string='Sequence')
    code = fields.Char(string='Vendor Status')
    status_change_user_ids = fields.Many2many('res.users')
    prevent_po_creation = fields.Selection(selection=[('yes','Yes'),('no','No'),('alert','Alert')], string='Prevent PO Creation')
    notify_user_id = fields.Many2one('res.users', string='Notify User')

    @api.model
    def _name_search(self, name, domain=None, operator='ilike', limit=None, order=None):
        domain = domain or []
        partner_id = self.env.context.get('partner_id')
        if not partner_id:
            sequence = self.env['vendor.status'].search([],order='sequence',limit=1).mapped('sequence')
            domain.append(('sequence', 'in', sequence))
        else:
            vendor = self.env['res.partner'].browse(partner_id)
            sequence_data= self.env['vendor.status'].search_read([('sequence', '>', vendor.vendor_status_id.sequence)],['sequence'],order='sequence',limit=1)
            domain.append(('sequence', '=', sequence_data[0]['sequence'])) if sequence_data else domain.append(('sequence', '=', False))
        return super()._name_search(name, domain, 'ilike', limit, order)

    @api.model
    def web_search_read(self, domain, specification, offset=0, limit=None, order=None, count_limit=None):
        if not self.env.context.get('vendor_status'):
            domain = domain or []
            partner_id = self.env.context.get('partner_id')
            if not partner_id:
                sequence = self.env['vendor.status'].search([],order='sequence',limit=1).mapped('sequence')
                domain.append(('sequence', 'in', sequence))
            else:
                vendor = self.env['res.partner'].browse(partner_id)
                sequence_data= self.env['vendor.status'].search_read([('sequence', '>', vendor.vendor_status_id.sequence)],['sequence'],order='sequence',limit=1)
                domain.append(('sequence', '=', sequence_data[0]['sequence'])) if sequence_data else domain.append(('sequence', '=', False))
        return super().web_search_read(domain, specification, offset=offset, limit=limit, order=order, count_limit=count_limit)
