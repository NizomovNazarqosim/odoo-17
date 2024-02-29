from odoo import models, fields, api


class Teacher(models.Model):
    _name = 'edu.teacher'
    _description = 'Teachers'

    name = fields.Char(string='Name', required=True)
    courses = fields.Many2many('edu.course', string='Courses')