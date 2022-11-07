from odoo import models, fields, api, _
from datetime import timedelta,datetime
from odoo.exceptions import UserError
import logging
_logger = logging.getLogger(__name__)

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description="estate.property.offer"
    _offer = 'price desc'

    price = fields.Float()
    status = fields.Selection(
        string='Status',
        copy=False,
        selection=[('Accepted', 'Accepted'), ('Refused', 'Refused')])
    partner_id = fields.Many2one("res.partner", string="Partner" , required=True)
    property_id = fields.Many2one("estate.property", string="Property", required=True)
    property_type_id = fields.Many2one(
        'estate.property.type',
        string="Estate Type",
        related='property_id.property_type_id',
        store=True
    )
    validity = fields.Integer()
    date_deadline = fields.Date(compute="_compute_date_deadline", inverse='_inverse_compute_date_deadline')
    

    
    _sql_constraints = [
        ('check_price', 'CHECK(price > 0)',
         'price should be more than 1.')
    ]

    @api.depends('validity')
    def _compute_date_deadline(self):
        for line in self:
            if line.create_date:
                line.date_deadline = line.create_date + timedelta(days=line.validity)
            else:
                line.date_deadline = datetime.today() + timedelta(days=line.validity)
    
    def _inverse_compute_date_deadline(self):
        for line in self:
            if line.create_date:
                frm_create_date = datetime.strptime(str(line.create_date), '%Y-%m-%d %H:%M:%S.%f')
                frm_date_deadline = datetime.strptime(str(line.date_deadline), '%Y-%m-%d')
                line.validity = (frm_date_deadline - frm_create_date).days

    def offer_accept(self):
        self.property_id.selling_price = self.price
        self.property_id.buyer_id = self.partner_id
        self.property_id.state = 'Offer accepted'
        self.status = 'Accepted'
        return True
    def offer_refuse(self):
        self.property_id.buyer_id = None
        self.status = 'Refused'
    
    @api.model
    def create(self, vals):
        estate_property = self.env['estate.property'].browse(vals['property_id'])
        offers = self.env['estate.property.offer'].search([('property_id','=',vals['property_id'])])
        if estate_property and len(offers):
            if vals.get('price') < max(d.price for d in offers):
                raise UserError(_("Your offer price less than the previous"))
        if estate_property:
            estate_property.state = 'Offer Received'
        return super().create(vals)


