from dataclasses import field
from typing_extensions import Required
from pkg_resources import require
from traitlets import default
from odoo import models, fields

class TestModel(models.Model):
    _name = "test.model"
    _description = "Test Model for checking model"

    tester_name = fields.Text(default="Unknown")
    last_seen = fields.Date("Last Seen", default=lambda self: fields.Datetime.now())
    rank = fields.Integer()
    location = fields.Text()