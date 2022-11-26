import werkzeug

from odoo import http
from odoo.http import request
import logging
_logger = logging.getLogger(__name__)

class PropertyTag(http.Controller):
    @http.route('/property-tag', type="http", auth="user", website=True)
    def property_tag_form(self, **kwargs):
        _logger.info('property tag page is called')
        tags = request.env['estate.property.tag'].sudo().search([])
        return request.render('property.web_property_tag_form', {'tags': tags})

    @http.route('/create-property-tag', type="http", auth="public", website=True)
    def create_property_tag(self, **kwargs):
        _logger.info('Send data be like %s', kwargs)
        result = request.env['estate.property.tag'].sudo().create({'name': kwargs.get('name'), 'color': kwargs.get('color')})
        _logger.info('Create result be like %s', result)
        tags = request.env['estate.property.tag'].sudo().search([])
        return request.render('property.web_property_tag_form', {'tags': tags})
