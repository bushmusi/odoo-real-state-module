# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Real Estate',
    'version': '1.2',
    'category': 'Estate/property',
    'sequence': 15,
    'summary': 'Create property and manage them',
    'description': "",
    'website': 'https://www.odoo.com/page/crm',
    'depends': [
        'base',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_property_type.xml',
        'views/estate_property_tag.xml',
        'views/estate_property_offer.xml',
        'views/estate_menus.xml',
    ],
    'css': ['static/src/css/crm.css'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'sequence': 0,
    'application': True,
}