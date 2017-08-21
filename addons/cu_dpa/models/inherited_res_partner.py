
# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class Partner(models.Model):
    _inherit = 'res.partner'

    city_id = fields.Many2one(
        string=u'City',
        comodel_name='res.country.state.city',
        ondelete='set null',
    )

    city = fields.Char(
        compute='_compute_city',
        inverse='_inverse_city',
        search='_search_city'
    )

    @api.depends('city_id')
    def _compute_city(self):
        for partner in self:
            partner.city = partner.city_id.name

    def _inverse_city(self):
        city = self.env['res.country.state.city'].search([
            ('name', '=', self.city),
            ('state_id', '=', self.state_id.id)
        ])
        if not city.exists():
            raise UserError(msg=_(u'City not found or not according to state.'))
        self.city_id = city

    def _search_city(self, operator, value):
        return [('city_id.name', operator, value)]

    @api.onchange('country_id')
    def _onchange_country_id(self):
        if self.state_id.exists() and self.state_id.country_id != self.country_id:
            self.state_id = []
            self.city_id = []
            self.zip = None

        if self.country_id.exists():
            return {
                'domain': {
                    'state_id': [('country_id', '=', self.country_id.id)]
                }
            }
        else:
            return {
                'domain': {
                    'state_id': []
                }
            }

    @api.onchange('state_id')
    def _onchange_state_id(self):
        if self.city_id.exists() and self.city_id.state_id != self.state_id:
            self.city_id = []
            self.zip = None

        if self.state_id.exists():
            self.country_id = self.state_id.country_id
            return {
                'domain': {
                    'city_id': [('state_id', '=', self.state_id.id)]
                }
            }
        else:
            return {
                'domain': {
                    'city_id': []
                }
            }

    @api.onchange('city_id')
    def _onchange_city_id(self):
        if self.city_id.exists():
            self.state_id = self.city_id.state_id
            self.country_id = self.state_id.country_id
            self.zip = self.city_id.zip
