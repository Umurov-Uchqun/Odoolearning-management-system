from odoo import models, fields

class Student(models.Model):
    _name = 'users.student'
    _inherit = 'users.user'

    user_id = fields.Many2one(required=True)
    name = fields.Char(required=True)
    branch_id = fields.Many2one(required=True)
    balance = fields.Float(default=0)



