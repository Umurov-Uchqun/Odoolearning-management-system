from odoo import models, fields


class Group(models.Model):
    _name = 'education.group'

    name = fields.Char(required=True)
    building_id = fields.Many2one("building.building")
    teacher_ids = fields.Many2Many("users.teacher")
    lesson_ids = fields.Many2one("education.lesson")
    course_id = fields.Many2one("education.course")
    student_ids = fields.Many2many("education.student")
    status = fields.Selection([
        ('new', 'New'),
        ('active','Active'),
        ('finished','Finished'),
        ('frozen', 'Frozen'),
    ],default='new')
    max_capacity = fields.Integer(default=20)
    min_capacity = fields.Integer(default=5)


