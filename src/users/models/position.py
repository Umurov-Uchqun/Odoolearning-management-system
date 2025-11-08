from odoo import models, fields


class Position(models.Model):
    _name = "pos.position"
    _description = "Position"

    name = fields.Char(required=True)
