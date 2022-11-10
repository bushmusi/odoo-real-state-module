from odoo import models, fields, api, _
from odoo.tools.float_utils import float_compare
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)

class EmployeeWage(models.Model):
    _name = 'employee.wage'
    _description = "Employee salary change logic design"

    min_wage = fields.Float(required=True, string="Minimum wage")
    max_wage = fields.Float(
        required=True,
        string="Maximum wage"
    )
    company_id = fields.Many2one('res.company', 'Company', default=lambda self: self.env.company, required=True)
    job_id = fields.Many2one('hr.job', 'Job Position', domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]")

    _sql_constraints = [
        ('job_id_unique', 'unique(job_id)', 'Can\'t be duplicate Job position!'),
        ('check_min_wage','CHECK(min_wage > 0)', 'Minimum wage should be greater than zero'),
        ('check_max_wage','CHECK(max_wage > 0)', 'maximum wage should be greater than zero'),
    ]

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
        """ We don't want the current user to be follower of all created job """
        employee_wage = self.env['employee.wage'].search([('job_id', '=', self.job_id.id)])
        _logger.info('employee wage: %s', employee_wage)
        if employee_wage:
            min_wage = int(employee_wage.min_wage)
            max_wage = int(employee_wage.max_wage)
            wage = int(self.wage)
            _logger.info('min: %s max: %s wage: %s', min_wage, max_wage, wage)
            _logger.info('is in range: %s', (wage in range(min_wage, max_wage)))
            if not wage in range(min_wage, max_wage):
                return {'warning': {
                    'title': _("Warning"),
                    'message': ('For ',self.job_id.name,' salary should be range of ' , min_wage ,' to ' , max_wage)}}