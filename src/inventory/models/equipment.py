from odoo import models,fields

class Equipment(models.Model):
    _name = 'inventory.equipment'
    _description = 'Equipment'

    name = fields.Char(required=True)
