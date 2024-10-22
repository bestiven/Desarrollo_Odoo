# -*- coding: utf-8 -*-

from odoo import fields, models

class Product(models.Model):
    _name = "taller.carros"
    _description = 'Registro de carros'

    customer_id = fields.Many2one("res.partner",string="Customer", required=True)

    country_id = fields.Many2one(string="customer country", related="customer_id.country_id" )
    city = fields.Char(string="ciudad", related="customer_id.city", required=True)

    field1 = fields.Char()
    marca = fields.Char(string='Marca', readonly=True,default="new" )
    matricula = fields.Char(string='Matricula',required=True, help="ingrese la matricula del veihiculo", size=10)
    email = fields.Char(string='Correo electrónico', help='Correo del empleado', readonly=True, default='prueba')
    tipoAuto = fields.Char(string='tipo de auto')
    km = fields.Integer(string="km")
    brand = fields.Many2one( "taller.brand",string="brand" )

