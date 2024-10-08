# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    #  Information
    'name': " WSCS - Vendor Extension",
    'version': '17.0.1.0',
    'category': 'Customization',
    'summary': "Extension for vendors",
    'description': """
WSCS - Vendor Extension| TaskID:4206547
---------------------------------------
The goal of this module is to extend vendor contacts including vendor status, gfsi scheme, grade and certification.
""",
    # Author
    'author': 'Odoo PS',
    'website': 'https://www.odoo.com',
    'license': 'LGPL-3',

    # Dependency
    'depends': ['purchase','wscs_product_extension'],

    'data': [
        'security/ir.model.access.csv',

        'views/res_partner.xml',
        'views/gfsi_scheme.xml',
        'views/gfsi_grade.xml',
        'views/gfsi_certification.xml',
        'views/vendor_status.xml',
        'views/product_supplierinfo_views.xml',
        'views/purchase_view.xml',
    ],
    # Other
    'installable': True,
}
