from odoo import models, fields

class Building(models.Model):
    _name = 'building.building'
    _description = 'Building'

    name = fields.Char(required=True)
    address = fields.Char(required=True)
    company_id = fields.Many2one("res.company",string="Company")
    floor_ids = fields.Many2one("building.floor",string="Floors")
