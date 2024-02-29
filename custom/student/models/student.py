from odoo import models, fields, api


class Studdent(models.Model):
    _name = 'edu.student'
    name = fields.Char(string="Student name", required=True)
    groups = fields.Many2many('edu.group', string='Groups')
    

