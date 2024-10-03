# -*- coding: utf-8 -*-

from odoo import fields, models, api


class RepairOrderLine(models.Model):
    _name = 'taller.repair.order.line'

    order_id = fields.Many2one( comodel_name="taller.repair.order")
    qty = fields.Float(string="Quantity")
    product_id = fields.Many2one(comodel_name="product.product",
                                 string="Product")

    price_unit = fields.Float('Unit Price', required=True,
                              digits='Product Price', default=0.0)

    currency_id = fields.Many2one('res.currency', string='Currency', required=True)
    price_subtotal = fields.Monetary(compute='_compute_amount',string='Subtotal', currency_field='currency_id')


@api.depends('product_uom_qty', 'discount', 'price_unit', 'tax_id')
def _compute_amount(self):
    """
    Compute the amounts of the SO line.
    """
    for line in self:
        # sin discount por ahora
        price = line.price_unit * line.qty
        line.price_subtotal = price

