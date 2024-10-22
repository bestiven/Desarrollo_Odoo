# -*- coding: utf-8 -*-

from odoo import fields, models

class OrderRepair(models.Model):
    _name = "taller.repair.order"
    _description = 'Taller repair order'

    customer_id = fields.Many2one("res.partner",string="Customer",required=True)

    name = fields.Char(string="Name", default="New")
    date = fields.Date(string="Date Order")

    line_ids = fields.One2many("taller.repair.order.line", inverse_name="order_id")






