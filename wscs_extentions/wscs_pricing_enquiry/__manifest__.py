# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': "WSCS - Pricing Enquiry",
    'version': '17.0.1.0.0',
    'category': 'Customizations',
    'summary': "Product Extension for Product Status and Pallet Specification",
    'description': """
WSCS - Pricing Enquiry | TaskID: 4206548
==========================================
The goal of this module is to extend inventory products, product categories and
product packaging for product status and product pallet specification.
    """,
    'depends': ['wscs_vendor_extension', 'wscs_product_extension'],
    'data': [
        'security/ir.model.access.csv',

        'data/data.xml',

        'views/enquiry_status_views.xml',
        'views/price_enquiry_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'wscs_pricing_enquiry/static/src/views/price_enquiry_dashboard.js',
            'wscs_pricing_enquiry/static/src/views/price_enquiry_listview.js',
            'wscs_pricing_enquiry/static/src/views/price_enquiry_listview.xml',
            'wscs_pricing_enquiry/static/src/views/price_enquiry_dashboard.xml',
        ],
    },
    'author': 'Odoo PS',
    'website': 'https://www.odoo.com',
    'license': 'LGPL-3',
    'installable': True,
}
