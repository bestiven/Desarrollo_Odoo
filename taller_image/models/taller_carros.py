# -*- coding: utf-8 -*-

from odoo import fields, models

class Product(models.Model):
    _inherit = "taller.carros"

    image= fields.Image(string="image")



