from odoo import models, fields

class Employee(models.AbstractModel):
    _name = "users.employee"
    _inherit = "users.user"

    user_id = fields.Many2one('res.users')
    work_place_ids = fields.Many2many("")
    experience_year = fields.Float()
    married = fields.Boolen(default=False)
    children_count = fields.Integer()
    building_id = fields.Many2one("")
    position_id = fields.Many2one("pos.position",string="Position")