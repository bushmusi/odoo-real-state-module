from odoo import models, fields
from datetime import timedelta

class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'This the main model for estate property'

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(
        "Last Seen", 
        default=lambda self: fields.Date.today() + timedelta(days=90),
        copy=False
    )
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(
     readonly=True,
     copy=False
    )
    bedrooms = fields.Integer(
        default=2
    )
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    graden_orentation = fields.Selection(
        string='Garden Orentation',
        selection=[('North', 'North'), ('South', 'South'),
                ('West','West'), ('East', 'East')],
        help="Type is used to separate garden orentation")
    active = fields.Boolean(
        default=True
    )
    state = fields.Selection(
        selection=[('New','New'),('Offer Received', 'Offer Received'),('offer accepted','offer accepted'),('Sold','Sold'),('Canceled','Canceled')],
        required=True,
        copy=False,
        default="New"
    )
    buyer_id = fields.Many2one("res.partner", string="Buyer")
    salesperson_id = fields.Many2one('res.users', string='Salesperson', index=True, tracking=True, default=lambda self: self.env.user)
    tag_ids = fields.Many2many("estate.property.tag", string="tages")
    offer_ids = fields.Many2many("estate.property.offer", string="Offers")