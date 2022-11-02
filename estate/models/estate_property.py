from traitlets import default
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from odoo.tools.float_utils import float_compare, float_is_zero
import logging
_logger = logging.getLogger(__name__)

class EstateProperty(models.Model):
    _name="estate.property"
    _description="It is managing to estate property"
    _order = "id desc"

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
        selection=[('New','New'),('Offer Received', 'Offer Received'),('offer accepted','offer accepted'),('Sold','Sold'),('Canceled','Canceled')],
        required=True,
        copy=False,
        default="New"
    )
    _sql_constraints = [
        ('check_selling_price', 'CHECK(selling_price >= 0 )',
            'The selling price must be posetive')
    ]
    _sql_constraints = [
        ('check_expected_price', 'CHECK(expected_price >= 0 )',
            'The expected price must be posetive')
    ]

    @api.depends('garden_area', 'living_area')
    def _compute_total_area(self): 
        for line in self:
            line.total_area = line.garden_area + line.living_area
    
    @api.depends('offer_ids.price')
    def _compute_best_price(self):
        for record in self:
            record.best_price = max(record.mapped('offer_ids.price'), default=0)

    @api.onchange("garden")
    def _onchange_partner_id(self):
        if self.garden:
            self.garden_area = 10
            self.garden_orientation = "North"
        else:
            self.garden_area = 0
            self.garden_orientation = ""

    def sell_property(self):
        _logger.info('sell property from parent')
        for record in self:
            if record.state == "Canceled":
                raise UserError(_("You can't set Caceled property as sold"))
            # else:
            #     record.state = "Sold"
        return True
    def cancel_property(self):
        for record in self:
            if record.state == "Sold":
                raise UserError(_("You can't set Sold property as Canceled"))
            else:
                record.state = "Canceled"
        return True
    @api.constrains('selling_price')
    def check_selling_price(self):
        for line in self:
            minimum_price = 0.9 * line.expected_price
            if float_compare(line.selling_price, minimum_price, precision_digits=2) <= 0 and not float_is_zero(line.selling_price, precision_digits=2):
                raise ValidationError(_('The selling price should be at least 90% ,of expected price'))
            elif float_compare(line.selling_price, minimum_price, precision_digits=2) == 0:
                print('value1 is equal to value2')
            else:
                print('value1 is greater than value2')

    def unlink(self):
        for record in self:
            if record.state not in ['New', 'Canceled']:
                raise ValidationError(_('Only New and Canceled property can be deleted'))
            record.offer_ids.unlink()
        return super(EstateProperty, self).unlink()




