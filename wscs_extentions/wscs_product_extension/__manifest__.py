# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': "WSCS - Product Extension",
    'version': '17.0.1.0.0',
    'category': 'Customizations',
    'summary': "Product Extension for Product Status and Pallet Specification",
    'description': """
WSCS - Product Extension | TaskID: 4206548
==========================================
The goal of this module is to extend inventory products, product categories and
product packaging for product status and product pallet specification.
    """,
    'depends': ['stock_delivery'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_palletspec_view.xml',
        'views/product_status_views.xml',
        'views/product_template_views.xml',
        'views/product_packaging_views.xml',
        'views/product_category_views.xml',
    ],
    'author': 'Odoo PS',
    'website': 'https://www.odoo.com',
    'license': 'LGPL-3',
    'installable': True,
}
