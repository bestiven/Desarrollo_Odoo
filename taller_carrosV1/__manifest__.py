# -*- coding: utf-8 -*-

{
    'name': "Modulo",
    'version': '1.0',
    'depends': ['base'],
    'author': "Bryan",
    'category': 'Category',
    'description': """
    Modulo de carros
    """,
    # data files always loaded at installation
    'data': [
     'data/cargaDeDatos.xml',
     'security/groups.xml',
     'security/ir.model.access.csv',
     'views/view_taller_carros.xml',
     'views/view_repair_order.xml',



    ],
    # data files containing optionally loaded demonstration data
    'demo': [

    ],
}

