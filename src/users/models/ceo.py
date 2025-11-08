from odoo import models, fields

class Ceo(models.Model):
    _name = "users.ceo"
    _inherit = "users.employee"

    user_id = fields.Many2one("res.users",string="User")


