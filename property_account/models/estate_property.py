from odoo import models,fields
import logging
_logger = logging.getLogger(__name__)

class EstateProperty(models.Model):
    _inherit = "estate.property"

    def sell_property(self):
        # _logger.info(" reached ".center(100, '='))
        # self.env['estate.property'].check_access_rights('update')
        journal = self.sudo().env['account.journal'].search([("type", "=", "sale")])
        price_unit = 0.06 * self.selling_price
        obj = self.sudo().env['account.move'].create({
                'type': 'out_invoice',
                'partner_id': self.salesperson_id,
                'journal_id': journal.id,
                'invoice_date': fields.Date.from_string('2016-01-01'),
                'invoice_line_ids': [
                    (0, None, {
                        'product_id': self.id,
                        'name': self.name,
                        'quantity': 1,
                        'price_unit': price_unit
                    }),
                    (0, None, {
                        'product_id': self.id,
                        'name': self.name,
                        'quantity': 1,
                        'price_unit':  100,
                    }),
                ]
        })
        return super().sell_property()