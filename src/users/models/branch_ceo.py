from odoo import models, fields

class BranchCeo(models.Model):
    _name = "users.branchceo"
    _inherit = "users.employee"

    user_id = fields.Many2one("res.users",string="User")
    branch_id = fields.Many2one("pos.branch",string="Branch")