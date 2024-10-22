# -*- coding: utf-8 -*-


from odoo import fields, models


class modelBrand(models.Model):
    _name = 'taller.brand'
    _description = 'taller.brand'

    name = fields.Char(string="Name",default="Nuevo Campo")
    image = fields.Binary(String="imagen")