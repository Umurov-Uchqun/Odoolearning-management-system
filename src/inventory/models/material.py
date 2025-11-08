from odoo import models, fields

class Material(models.Model):
    _name = 'inventory.material'
    _description = 'Material'

    name = fields.Char(required=True)
