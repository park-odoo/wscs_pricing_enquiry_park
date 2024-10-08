# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models, _
from odoo.exceptions import AccessError


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    @api.model_create_multi
    def create(self, vals_list):
        records = super(PurchaseOrder, self).create(vals_list)
        for record, vals in zip(records, vals_list):
            vendor = self.env['res.partner'].browse(vals.get('partner_id'))
            po_prevention = vendor.vendor_status_id.prevent_po_creation
            if po_prevention == 'yes':
                raise AccessError(_('You cannot create a purchase order with %(vendor_status)s vendor status',
                                    vendor_status=vendor.vendor_status_id.code))
            elif po_prevention == 'alert':
                notify_user = vendor.vendor_status_id.notify_user_id
                if notify_user:
                    record.message_post(
                        body=_('Purchase Order created with vendor status: %(vendor_status)s. Notified user: %(user)s',
                                vendor_status=vendor.vendor_status_id.code, user=notify_user.name),
                                partner_ids=[notify_user.partner_id.id]
                        )
                raise AccessError(_('You cannot create a purchase order with %(vendor_status)s vendor status',
                                    vendor_status=vendor.vendor_status_id.code))
            elif po_prevention == 'no' and vendor.is_gfsi_certification == 'yes' and vendor.is_fsc_certified == 'yes' and vendor.is_pefc_certified == 'yes':
                vendor.vendor_status_id = self.env['vendor.status'].search([('prevent_po_creation','=','no')], order='sequence desc', limit=1).id
        return records
