from odoo import models, fields

class Homework(models.Model):
    _name = 'education.homework'
    _description = 'Homework'

    group_id = fields.Many2one('education.group')
    teacher_id = fields.Many2one('users.teacher')
    deadline = fields.Datetime('deadline')
