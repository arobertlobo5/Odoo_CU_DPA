
# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from odoo import models, fields, api


class Company(models.Model):
    _inherit = 'res.company'

    city_id = fields.Many2one(
        string=u'City',
        comodel_name='res.country.state.city',
        compute='_compute_city_id',
        inverse='_inverse_city_id'
    )

    @api.multi
    @api.depends('partner_id.city_id')
    def _compute_city_id(self):
        for company in self:
            company.city_id = company.partner_id.city_id

    def _inverse_city_id(self):
        self.partner_id.city_id = self.city_id

    @api.onchange('city_id')
    def _onchange_city_id(self):
        if self.city_id.exists():
            self.state_id = self.city_id.state_id
            self.country_id = self.state_id.country_id
            self.zip = self.city_id.zip

    @api.onchange('state_id')
    def _onchange_state(self):
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

    @api.onchange('country_id')
    def _onchange_country_id_wrapper(self):
        if self.state_id.exists() and self.state_id.country_id != self.country_id:
            self.state_id = []
            self.city_id = []
            self.zip = None

        # Original from Odoo
        values = self.on_change_country(self.country_id.id)['value']
        for fname, value in values.iteritems():
            setattr(self, fname, value)

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
