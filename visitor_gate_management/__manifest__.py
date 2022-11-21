# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2019-TODAY Cybrosys Technologies(<https://www.cybrosys.com>).
#    Author: Anusha P P (odoo@cybrosys.com)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################

{
    'name': "Visitor Gate Management",
    'version': '13.0.1.0.0',
    'summary': """Manage Visitor Gate Operations:Visitors, Devices Carrying Register, Actions""",
    'description': """Helps You To Manage Visitor Gate Operations, Odoo13, Odoo 13""",
    'author': "Tria trading plc",
    'maintainer': 'Bushra Mustofa',
    'company': "Tria trading plc",
    'website': "http://triaplc.com/",
    'category': 'Industries',
    'depends': ['base', 'hr', 'web_notify'],
    'data': [
        'views/fo_visit.xml',
        'views/fo_visitor.xml',
        'views/email_appointment_templates.xml',
        'views/fo_property_counter.xml',
        'report/report.xml',
        'report/fo_property_label.xml',
        'report/fo_visitor_label.xml',
        'report/visitors_report.xml',
        'security/fo_security.xml',
        'security/ir.model.access.csv',
    ],
    'images': ['static/description/banner.png'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
    'sequence': 0,
}
