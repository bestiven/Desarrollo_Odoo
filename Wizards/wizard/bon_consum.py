# -*- coding: utf-8 -*-

from odoo import models,fields

class BonConsum (models.TransientModel):
    _name = "bon.consum"

    data_from = fields.Date(string="Fecha")
    date_to = fields.Date(string="dato fecha")
    analytic_account_id = fields.Many2one(comodel_name="account.analytic.account")

    def action_print_report(self):
        pass






