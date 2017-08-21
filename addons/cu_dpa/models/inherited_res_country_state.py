
# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from odoo import models, fields


class CountryState(models.Model):
    _inherit = 'res.country.state'

    acronym = fields.Char("Acronym")
