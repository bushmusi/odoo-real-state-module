from odoo import models, fields, api, _
from odoo.tools.float_utils import float_compare
from odoo.exceptions import ValidationError, UserError
import logging
_logger = logging.getLogger(__name__)

class EmployeeWage(models.Model):
    _name = 'hr.job'
    _inherit = 'hr.job'
    _description = "Employee salary change logic design"

    min_wage = fields.Float(required=True, string="Minimum wage")
    max_wage = fields.Float(
        required=True,
        string="Maximum wage"
    )

    _sql_constraints = [
        ('job_id_unique', 'unique(job_id)', 'Can\'t be duplicate Job position!'),
        ('check_min_wage','CHECK(min_wage > 0)', 'Minimum wage should be greater than zero'),
        ('check_max_wage','CHECK(max_wage > 0)', 'maximum wage should be greater than zero'),
        ('check_max_wage_greater_than_min_wage','CHECK(max_wage > min_wage)', 'maximum wage should be greater than zero'),
    ]

    @api.constrains('selling_price')
    def _check_max_wage(self):
        if self.max_wage < self.min_wage:
            raise UserError(_('Maximum wage should be greater than minimum wage'))

    @api.model
    def create(self, vals):
        _logger.info('min wage: %s max wage: %s',vals['min_wage'], vals['max_wage'])
        if float_compare(vals['min_wage'], vals['max_wage'], precision_digits=2) == 1:
            raise ValidationError(_('Maximum wage should be greater than minimum wage'))
        return super().create(vals)

class WageControl(models.Model):
    _inherit = 'hr.contract'
    
    @api.onchange('wage')
    def _compute_wage_validation(self):
        employee_wage = self.env['hr.job'].search([('id', '=', self.job_id.id)])
        if employee_wage:
            min_wage = int(employee_wage.min_wage)
            max_wage = int(employee_wage.max_wage)
            wage = int(self.wage)
            _logger.info('min: %s max: %s wage: %s', min_wage, max_wage, wage)
            _logger.info('is in range: %s', (wage in range(min_wage, max_wage)))
            if not wage in range(min_wage, max_wage):
                return {'warning': {
                    'title': _("Warning"),
                    'message': ('For '+str(self.job_id.name)+' salary should be range of ' + str(min_wage) + ' to '+str(max_wage))}}