from odoo import models, fields

class Teacher(models.Model):
    _name = 'users.teacher'
    _inherit = "users.employee"
    user_id = fields.Many2one("res.users")
    subject_id = fields.Many2many(
        'education.subject', )
    group_id = fields.Many2one("groups.group")
    salary = fields.Float(required=True)


