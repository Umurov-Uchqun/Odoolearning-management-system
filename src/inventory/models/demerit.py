from odoo import models, fields

class Demerit(models.Model):
    _name = 'inventory.demerit'
    _description = 'Demerit'

    name = fields.Char(required=True)