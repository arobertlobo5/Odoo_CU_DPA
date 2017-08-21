
# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from odoo import models, fields


class City(models.Model):
    """ City from country state.

    Fields:
      name (Char): Human readable name which will identify city.
      code (Char): City code for country state.
      state_id (Many2one): Reference to country state.

    """

    _name = 'res.country.state.city'
    _description = u'City from country state'

    _rec_name = 'name'
    _order = 'name ASC'

    name = fields.Char(
        u'City name',
        required=True,
        help=u'City from country state according to political and administrative division.'
    )

    code = fields.Char(
        u'Code',
        help=u'City code for country state.'
    )

    zip = fields.Char(
        string=u'ZIP',
        help=u'Post code (ZIP) for city.'
    )

    state_id = fields.Many2one(
        string=u'State',
        comodel_name='res.country.state',
        ondelete='cascade',
    )

    create_uid = fields.Many2one(
        string=u'Created by',
        comodel_name='res.country.state',
        default=lambda self: self.env.user
    )

    create_date = fields.Date(
        string=u'Created at',
        default=fields.Date.context_today,
    )

    company_id = fields.Many2one(
        string=u'Company',
        comodel_name='res.company',
        required=True,
        default=lambda self: self.env.user.company_id
    )
