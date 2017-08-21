# -*- coding: utf-8 -*-
{
    'name': "Cuba - División Político Administrativa",

    'summary': """
        República de Cuba - DPA""",

    'description': u"""
República de Cuba - DPA
=======================


Provee la División Político-Administrativa (DPA) actualizada conforme a la codificación aprobada por la 
**Oficina Nacional de Estadísticas e Información** (ONEI).

Características añadidas:

#.  Municipios y su código (clasificador DPA-ONEI).
#.  Provincias, sigla y su código (clasificador DPA-ONEI). 
#.  Código Postal de cada municipio. 
#.  Integración con los formularios de *res.partner* y *res.company*.

Fuente: http://www.onei.gob.cu
    """,

    'author': "Ing. Armando Robert Lobo",
    'website': "http://www.github.com/arobertlobo5",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Localization',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',

        'data/res.country.state.csv',
        'data/res.country.state.city.csv',

        'views/inherited_res_company_views.xml',
        'views/inherited_res_partner_views.xml',
        'views/inherited_res_country_views.xml',
        'views/city_views.xml'
    ],

    # only loaded in demonstration mode
    'demo': [],
}