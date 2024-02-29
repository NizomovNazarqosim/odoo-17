from odoo import models, fields, api

class Group(models.Model):
    _name = 'edu.group'
    name = fields.Char(string="Group name", required=True)
    course_id = fields.Many2one('edu.course', string='Course')
    teacher_id = fields.Many2one('edu.teacher', string='Teacher')
    students = fields.Many2many('edu.student', string='Students')