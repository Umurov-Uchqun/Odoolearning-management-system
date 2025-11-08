from odoo import models, fields

class Floor(models.Model):
    _name = 'building.floor'


    name = fields.Char(required=True)
    building_id = fields.Many2one('building.building',required=True)
    room_ids = fields.One2many('building.room','floor_id',string="Rooms")