# -*- coding: utf-8 -*-
##############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#    Copyright (C) 2017-TODAY Cybrosys Technologies(<https://www.cybrosys.com>).
#    Maintainer: Cybrosys Technologies (<https://www.cybrosys.com>)
##############################################################################

from odoo import models, fields, api


class VisitorDetails(models.Model):
    _name = 'fo.visitor'

    name = fields.Char(string="Visitor", required=True)
    visitor_image = fields.Binary(string='Image', attachment=True)
    city = fields.Char()
    country_id = fields.Many2one('res.country', string='Country', ondelete='restrict')
    phone = fields.Char(string="Phone", required=True)
    email = fields.Char(string="Email")
    id_proof = fields.Many2one('id.proof', string="ID Proof")
    id_proof_no = fields.Char(string="ID Number", help='Id proof number')
    company_info = fields.Many2one('res.partner', string="Company", help='Visiting persons company details')
    visit_count = fields.Integer(compute='_no_visit_count', string='# Visits')

    _sql_constraints = [
        ('field_uniq_email_and_id_proof', 'unique (email,id_proof_no)', "Please make sure ID Proof or Email is unique !"),
    ]

    def _no_visit_count(self):
        data = self.env['fo.visit'].search([('visitor', 'in', self.ids), ('state', '!=', 'cancel')]).ids
        self.visit_count = len(data)


class VisitorProof(models.Model):
    _name = 'id.proof'
    _rec_name = 'id_proof'

    id_proof = fields.Char(string="Name")
    code = fields.Char(string="Code")








