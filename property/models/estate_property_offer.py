from odoo import models, fields

class EstatePropertyTag(models.Model):
    _name = "estate.property.offer"
    _description="estate.property.offer"

    price = fields.Float()
    status = fields.Selection(
        string='Status',
        copy=False,
        selection=[('Accepted', 'Accepted'), ('Refused', 'Refused')])
    partner_id = fields.Many2one("res.partner", string="Partner" , required=True)
    property_id = fields.Many2one("estate.property", string="Property", required=True)