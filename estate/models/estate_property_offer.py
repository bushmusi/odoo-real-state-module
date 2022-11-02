from audioop import reverse
from traitlets import default
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from datetime import date, timedelta, datetime
import logging
_logger = logging.getLogger(__name__)

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Estate Property Offer"
    _order = "price desc"

    price = fields.Float()
    status = fields.Selection(
        selection=[('Accepted','Accepted'),('Refused', 'Refused'),('sold','Sold')],
        copy=False
    )
    partner_id = fields.Many2one('res.partner', string="Partner", required=True)
    property_id = fields.Many2one('estate.property', string="Estate Property", required=True)
    property_type_id = fields.Many2one('estate.property.type', string="Estate Type", related="property_id.property_type_id")
    date_deadline = fields.Date(default=lambda self: fields.Datetime.today() + timedelta(days=90))
    valid = fields.Integer(compute="_compute_valid", inverse="_inverse_valid")
    _sql_constraints = [
        ('check_price', 'CHECK(price >= 0 )',
            'The price must be posetive')
    ]
    
    @api.depends('date_deadline')
    def _compute_valid(self):
        _logger.debug("compute valid mode")
        for line in self:
            line.valid=0
            if line.date_deadline:
                fmt = '%Y-%m-%d'
                d1 = datetime.today()
                if line.create_date:
                    d1 = datetime.strptime(str(line.create_date), '%Y-%m-%d %H:%M:%S.%f')
                d2 = datetime.strptime(str(line.date_deadline), fmt)
                line.valid = (d2 - d1).days
    
    def _inverse_valid(self):
        _logger.debug("inverse mode")
        for line in self: 
            fmt = '%m-%d-%Y'
            d1 = datetime.today()
            line.date_deadline = d1 + timedelta(days=line.valid)

    def action_accept(self):
        for line in  self:
            line.property_id.selling_price = line.price
            line.property_id.buyer_id = line.partner_id
            line.property_id.state = "Offer Received"
            line.status = "Accepted"
    def action_refuse(self):
        for line in  self:
            line.property_id.selling_price = 0
            line.property_id.buyer_id = None
            line.status = "Refused"
    
    @api.model
    def create(self, vals):
        _logger.info('Create a %s with vals %s', self._name, vals)
        estate_property_offer = self.env['estate.property.offer'].search([('property_id', '=', vals.get('property_id'))])
        if estate_property_offer:
            if vals.get('price') < max(d.price for d in estate_property_offer):
                _logger.info('compare price and best %s with vals %s', vals.get('price'), max(d.price for d in estate_property_offer))
                raise UserError(_("Your offer price less than the previous"))
        return super().create(vals)
        
    