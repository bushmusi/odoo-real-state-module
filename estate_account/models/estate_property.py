from odoo import models
import logging
_logger = logging.getLogger(__name__)

class EstateProperty(models.Model):
    _inherit = "estate.property"

    def sell_property(self):
        _logger.info('sell property from child')
        return super().sell_property()