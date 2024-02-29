from odoo import models, fields, api

class Admin(models.Model):
    _name = 'edu.admin'
    _description = 'Admin Model'

    name = fields.Char(string='Name', required=True)
    role = fields.Char(string='Role', required=True)