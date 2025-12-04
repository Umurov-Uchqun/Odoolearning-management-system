from odoo import models, fields, api


class Group(models.Model):
    """
    FSWD - 1
    """
    _name = "le.group"
    _description = "Group"

    name = fields.Char(string="Name", required=True)
    course_id = fields.Many2one("le.course", string="Course", required=True)
    group_student_ids = fields.One2many("le.group.student", "group_id", string="Students")
    schedule_table_ids = fields.One2many(
        'le.schedule.table',
        'group_id',
        string='Schedule Table'
    )
    @api.model_create_multi
    def create(self, vals_list):
            return super(Group, self).create(vals_list)

