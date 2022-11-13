from odoo import models, fields, api, _
from datetime import timedelta
from odoo.tools.float_utils import float_compare, float_is_zero
from odoo.exceptions import UserError, ValidationError
import logging
_logger = logging.getLogger(__name__)

class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'This the main model for estate property'
    _order = 'sequence, name '

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
        selection=[('New','New'),('Offer Received', 'Offer Received'),('Offer accepted','Offer accepted'),('Sold','Sold'),('Canceled','Canceled')],
        required=True,
        copy=False,
        default="New"
    )
    property_type_id = fields.Many2one('estate.property.type', string="Type")
    buyer_id = fields.Many2one("res.partner", string="Buyer")
    salesperson_id = fields.Many2one('res.users', string='Salesperson', index=True, tracking=True)
    tag_ids = fields.Many2many("estate.property.tag", string="tages")
    offer_ids = fields.One2many("estate.property.offer", "property_id", string="Offers")
    total_area = fields.Float(compute = "_compute_total_area")
    best_price = fields.Float(compute = "_compute_best_price")
    sequence = fields.Integer('Sequence', default=1, help="Used to order stages. Lower is better.")
    company_id = fields.Many2one('res.company', 'Company', default=lambda self: self.env.company, required=True)
    
    _sql_constraints = [
        ('check_selling_price', 'CHECK(selling_price >= 0)',
         'Selling price should be more than 1.'),
         
        ('check_expected_price', 'CHECK(expected_price >= 0)',
         'Expected price should be more than 1.')
    ]



    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        self.total_area = 0
        for record in self:
            record.total_area = record.living_area + record.garden_area
    
    @api.depends('offer_ids.price')
    def _compute_best_price(self):
        self.best_price = 0
        for line in self:
            if len(line.offer_ids) > 0:
                line.best_price = max(line.offer_ids.mapped('price'))

    @api.onchange('garden')
    def _onchange_garden(self):
        if self.garden:
            self.garden_area = 10
            self.graden_orentation = 'North'
        else:
            self.garden_area = 0
            self.graden_orentation = None
            # return {'warning': {
            #     'title': _("Warning"),
            #     'message': ('This option is not supported for Authorize.net')}}
    def sell_property(self):
        template = self.env.ref('auth_signup.mail_template_user_signup_account_created')
        for record in self:
            if record.state == 'Canceled':
                raise UserError(_('Cancelled property can\'t be sold'))
            record.state = 'Sold'
            email_values = {
                'email_cc': False,
                'email_to': 'bush7840@yahoo.com',
                'subject': 'Test Email'
            }
            template.send_mail(record.id, force_send=True, email_values = email_values)

            return True
    def cancel_property(self):
        for record in self:
            if record.state == 'Sold':
                raise UserError(_('Sold property can\'t be cancelled'))
            record.state = 'Canceled'
            return True
    @api.constrains('selling_price')
    def _check_selling_price(self):
        for line in self:
            min_price = 0.9 * line.expected_price
            if not float_is_zero(line.expected_price, precision_digits=2) and float_compare(min_price, line.selling_price, precision_digits=2) == 1:
                raise ValidationError(_("Selling price should be 90% of expeceted price"))
    
    def unlink(self):
        for line in self:
            if line.state not in ['New', 'Canceled']:
                raise ValidationError(_('Only new or canceled property can be deleted'))
            self.offer_ids.unlink()
        return super(EstateProperty, self).unlink()