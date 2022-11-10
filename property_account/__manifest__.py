# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Property Account',
    'version': '1.2',
    'category': 'Estate/property',
    'sequence': 0,
    'summary': 'This is link module between property and account',
    'description': "If you like to add detail desctiption add here pls",
    'website': 'https://www.odoo.com/page/crm',
    'depends': [
        'property',
        'account',
    ],
    'data': [
    ],
    'css': ['static/src/css/crm.css'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'sequence': 2,
    'application': True,
}