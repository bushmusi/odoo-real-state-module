from odoo import fields, models

class ResUsers(models.Model):
    _inherit = "res.users"

    property_ids = fields.One2many('estate.property', 'sales_person_id', 
    domain="['|', ('state', '=', 'New'), ('state', '=', 'Offer Received'), ('state', '=', 'offer accepted')]")