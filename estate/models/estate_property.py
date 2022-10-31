from traitlets import default
from odoo import models, fields, api

class EstateProperty(models.Model):
    _name="estate.property"
    _description="It is managing to estate property"

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availabilty = fields.Char(string="Availability From",  default=lambda self: fields.Datetime.today(), copy=False)
    # expected_price = fields.Date(required=True)
    expected_price = fields.Integer(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    property_type_id = fields.Many2one("estate.property.type", string="Property Type")
    buyer_id = fields.Many2one('res.partner', string="Buyer", copy=False)
    tag_ids = fields.Many2many("real.property.tag", string="Tags")
    offer_ids = fields.One2many("estate.property.offer", "property_id", string="Offers")
    sales_person_id = fields.Many2one('res.users', string="Sales Person", default=lambda self: self.env.user)
    total_area = fields.Float(compute="_compute_total_area")
    best_price = fields.Float(compute="_compute_best_price")
    garden_orientation = fields.Selection(
        string='Garden Orentation',
        selection=[('North', 'North'), ('South', 'South'), ('West', 'West'), ('East', 'East')],
        help="Garden orentation should be automatic")
    active = fields.Boolean(default=True)
    state = fields.Selection(
        selection=[('New','New'),('Offer Received', 'Offer Received'),('sold','Sold'),('Canceled','Canceled')],
        required=True,
        copy=False,
        default="New"
    )

    @api.depends('garden_area', 'living_area')
    def _compute_total_area(self):
        for line in self:
            line.total_area = line.garden_area + line.living_area
    
    @api.depends('offer_ids.price')
    def _compute_best_price(self):
        for record in self:
            record.best_price = max(record.mapped('offer_ids.price'), default=0)


