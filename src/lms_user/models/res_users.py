from odoo import models, fields, api

class Users(models.Model):
    _inherit = 'res.users'

    user_type = fields.Selection([
        ('admin', 'Admin'),
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    ]
    )