# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Partner(models.Model):
    _inherit = 'res.partner'

    instructor_id = fields.Boolean(default=False)
    sessions_ids = fields.Many2many('openacademy.session', string="Attended Sessions", readonly=True)
    other_field = fields.Boolean(default=True)

    other_field2 = fields.Boolean(default=True)
