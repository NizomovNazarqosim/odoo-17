from odoo import models, fields, api

class Course(models.Model):
    _name = 'edu.course'
    _description = 'courses'

    name = fields.Char(string='Name', required=True)