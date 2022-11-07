from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class EstatePropertyType(models.Model):
    _name='estate.property.type'
    _description="estate.property.type"
    _order = 'name asc'

    name=fields.Char()
    property_ids = fields.One2many("estate.property", "property_type_id")
    offer_ids = fields.One2many("estate.property.offer", "property_type_id")
    offer_count = fields.Integer(
        compute='_compute_offer_count' )
    
    @api.depends('offer_ids')
    def _compute_offer_count(self):
        for record in self:
            record.offer_count = 0
            _logger.info('number of offer:%s', len(record.offer_ids))
            if len(record.offer_ids):
                record.offer_count = len(record.offer_ids)
    
    _sql_constraints = [
        ('check_name', 'UNIQUE(name)', 'A type must be unique!'),
    ]