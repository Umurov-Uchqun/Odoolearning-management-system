from odoo import models, fields

class Operator(models.Model):
    _name = 'users.operator'
    _inherit = 'users.employee'

    user_id = fields.Many2one('res.users', required=True)
    branch_id = fields.Many2one('building.building', required=True)
