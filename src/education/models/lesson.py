from odoo import models, fields

class Lesson(models.Model):
    _name = 'education.lesson'
    _description = 'Lesson'

    name = fields.Char(required=True)
    description = fields.Char(string='Description')

