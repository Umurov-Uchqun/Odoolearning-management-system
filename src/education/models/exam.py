from odoo import models, fields

class Exam(models.Model):
    _name = 'education.exam'

    name = fields.Char(required=True)
    group_id = fields.Many2one(comodel_name='group', required=True)
    teacher_id = fields.Many2one(comodel_name='teacher')
    exam_date = fields.Datetime(required=True)
    duration_minutes = fields.Integer(default=0)

