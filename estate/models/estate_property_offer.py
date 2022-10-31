from audioop import reverse
from traitlets import default
from odoo import models, fields, api
from datetime import date, timedelta, datetime

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Estate Property Offer"

    price = fields.Float()
    status = fields.Selection(
        selection=[('Accepted','Accepted'),('Refused', 'Refused'),('sold','Sold')],
        copy=False
    )
    partner_id = fields.Many2one('res.partner', string="Partner", required=True)
    property_id = fields.Many2one('estate.property', string="Estate Property", required=True)
    date_deadline = fields.Date(default=lambda self: fields.Datetime.today() + timedelta(days=90))
    valid = fields.Integer(compute="_compute_valid", inverse="_inverse_valid")
    
    @api.depends('date_deadline')
    def _compute_valid(self):
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
        for line in self: 
            fmt = '%m-%d-%Y'
            d1 = datetime.today()
            line.date_deadline = d1 + timedelta(days=line.valid)