from odoo import models, fields

class Hr(models.Model):
    _name = "users.hr"
    _inherit = "users.employee"

    user_id = fields.Many2one('res.users',required=True)
    branch_id = fields.Many2one(required=True)
