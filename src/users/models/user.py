from odoo import models, fields

class User(models.Model):
    _name = "users.user"
    _inherit = "res.users"

    passport = fields.Char()
    language_ids = fields.Many2many("edu.language")

