from odoo import fields, models

class RealPropertyTag(models.Model):
    _name = "real.property.tag"
    _description = "Estate Tag"
    _order = "name asc"

    name = fields.Char(required=True)
    color = fields.Char(string="Color")
    _sql_constraints = [
        ('tag_name',
         'unique (name)',
         'Tag name should be unique')
    ]