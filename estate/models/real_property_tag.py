from odoo import fields, models

class RealPropertyTag(models.Model):
    _name = "real.property.tag"
    _description = "Estate Tag"

    name = fields.Char(required=True)