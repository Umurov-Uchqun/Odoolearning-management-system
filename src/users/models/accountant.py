from odoo import models, fields

class Account(models.Model):
    _name = "users.user"
    _inherit = "users.employee"

    user_id = fields.Many2one('res.users',required=True)
    branch_id = fields.Many2one('building.building',required=True)