from odoo import models, fields

class Course(models.Model):
    _name = 'education.course'
    _description = 'Course'

    name = fields.Char(required=True)
    teacher_ids = fields.Many2many("users.teacher")
    lesson_ids = fields.One2many("education.lesson")
    group_ids = fields.One2many("education.group")
    lesson_number = fields.Integer(string="Lesson Number", compute="_compute_lesson_number")


    def _compute_lesson_number(self):
        pass