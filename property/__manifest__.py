# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Real Estate',
    'version': '1.2',
    'category': 'Real Estate/Brokerage',
    'sequence': 0,
    'summary': 'Create property and manage them',
    'description': "",
    'website': 'https://www.odoo.com/page/crm',
    'depends': [
        'base',
        'website',
    ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_property_offer.xml',
        'views/estate_property_type.xml',
        'views/estate_property_tag.xml',
        'views/users_view.xml',
        'views/estate_menus.xml',
        'views/web_template.xml',
        'views/web_tag_template.xml',
    ],
    'demo': [
        'demo/type_demo_data.xml',
        'demo/property_demo_data.xml',
        'demo/offer_demo_data.xml',
    ],
    'css': ['static/src/css/crm.css'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'sequence': 1,
    'application': True,
}