from odoo import http
from odoo.http import request

class MyController(http.Controller):
    @http.route('/some/url', website=True, auth='public')
    def handler(self, **kw):
        property = request.env['estate.property'].sudo().search([])
        return request.render('property.real_estate_template', {
            'property': property
        })