from odoo import models, fields

class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description="estate.property.tag"
    _order = 'name asc'

    name = fields.Char()
    color = fields.Integer(string="Color")
    _sql_constraints = [
        ('check_name', 'UNIQUE(name)', 'A tag must be unique!'),
    ]