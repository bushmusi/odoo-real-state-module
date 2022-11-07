from odoo import models, fields

class ResUsers(models.Model):
    _inherit = 'res.users'

    property_ids = fields.One2many('estate.property','salesperson_id',
        domain="['|', ('state', '=', 'New'), ('state', '=', 'Offer Received'), ('state', '=', 'offer accepted')]")