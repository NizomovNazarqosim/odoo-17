from odoo import models, fields, api

class Payment(models.Model):
    _name = 'edu.payment'
    date = fields.Date(string="Payment date", default=fields.Date.today())
    amount = fields.Float(string="Payment amount", required=True)
    comment = fields.Char(string="comment")
    student_id = fields.Many2one('edu.student', string='Student')
    state = fields.Selection([('draft', 'Draft'), ('accepted', 'Accepted')], string='state', default='draft')