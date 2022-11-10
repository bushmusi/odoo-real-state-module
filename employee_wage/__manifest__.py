# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Employee Wage Control',
    'version': '1.2',
    'sequence': 0,
    'summary': 'Employee wage control system',
    'description': "Here we will control wage salary range",
    'website': 'https://www.odoo.com/page/crm',
    'depends': [
        'hr_contract',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/employee_wage_views.xml',
        'views/employee_wage_menu.xml',
    ],
    'css': ['static/src/css/crm.css'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'sequence': 0,
    'application': True,
}