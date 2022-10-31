from odoo import models, fields

class BushProperty(models.Model):
    _name="bush.property"
    _description="It is managing to bush property"

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
