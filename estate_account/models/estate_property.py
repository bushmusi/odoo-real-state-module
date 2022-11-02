from odoo import models
import logging
_logger = logging.getLogger(__name__)

class EstateProperty(models.Model):
    _inherit = "estate.property"

    def sell_property(self):
        # _logger.info('sell property from child',self.get('buyer_id'))
        for record in self:
            journal = self.env['account.journal'].search([("type", "=", "sale")])
            _logger.info('model buyer id %s with record name %s journal id: %s', record.buyer_id, record.name, journal.id)
            writeoff_move = self.env['account.move'].with_context(default_move_type='out_invoice').create({
                'partner_id': record.buyer_id.id,
                'journal_id': journal.id,
                "invoice_line_ids": [
                    (
                        0,
                        0,
                        {
                            "name": "value_1",
                            "quantity": 5,
                            "price_unit": 1002.25,
                        },
                    )
                ],
            })
            _logger.info('created model is: %s', writeoff_move)
        return super().sell_property()