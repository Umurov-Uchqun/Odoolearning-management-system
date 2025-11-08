from odoo import models, fields

class Room(models.Model):
    _name = 'builder.room'
    _description = 'Room'

    name = fields.Char(required=True)
    building_id = fields.Many2one('building.building')
    floor_id = fields.Many2one('building.floor')
    capacity = fields.Integer(default=10)
    room_type = fields.Selection([
        ('classroom','Classroom'),
        ('office','Office'),
        ('coworking','Coworking')
    ],default='classroom')
