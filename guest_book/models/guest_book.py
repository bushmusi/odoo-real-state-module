# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError

import logging
_logger = logging.getLogger(__name__)


class GuestBook(models.Model):

    _name = "guest.book"
    _description = "Guest Book"
    _order = "create_date desc"
    _translate = True

    guest_number = fields.Char(
        string="Guest Number",
        readonly=True
    )
    name = fields.Char(
        string="Name",
        required=True,
        track_visibility='onchange'
    )
    gender = fields.Selection(
        string='Gender',
        selection=[('m', 'Male'), ('f', 'Female')],
        required=True,
        track_visibility='onchange'
    )
    phone = fields.Char(
        string='Phone',
        track_visibility='onchange'
    )
    email = fields.Char(
        string='Email',
        track_visibility='onchange'
    )
    institution = fields.Char(
        string='Institution',
        track_visibility='onchange'
    )
    meet = fields.Many2one(
        string='Meet',
        comodel_name='hr.employee',
        track_visibility='onchage'
    )
    purpose_id = fields.Many2one(
        string='Purpose',
        comodel_name='guest.book.purpose',
        track_visibility='onchange'
    )
    info = fields.Char(
        string='Info',
        track_visibility='onchange'
    )
    company_id = fields.Many2one(
        'res.company', string="Company",
        default=lambda self: self.env['res.company']._company_default_get('guest.book'))

    @api.model
    def create(self, vals):
        # Get next ticket number from the sequence
        vals['guest_number'] = self.env['ir.sequence'].next_by_code('guest.book')
        #Send an email out to employee in the meet
        new_id = super(GuestBook, self).create(vals)
        # import pdb; pdb.set_trace()
        template = self.env['ir.model.data'].sudo().get_object('guest_book', 'new_guest')
        template.send_mail(new_id.id, True)
        return new_id

class GuestBookPurpose(models.Model):

    _name = "guest.book.purpose"
    _description = "Guest Book Purpose"
    _order = "sequence desc"
    _translate = True

    sequence = fields.Integer(string="Sequence")
    name = fields.Char(required=True, translate=True, string="purpose")
    color = fields.Char(string="Color")
