# -*- coding: utf-8 -*-
{
    'name': "YU Movies",

    'summary': """
        """,

    'description': """
        俞元的电影demo模块
    """,

    'author': "",
    'website': "https://scofieldsu.github.io/",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'YU',
    'version': '0.1',
    'sequence': 1000,
    # any module necessary for this one to work correctly
    'depends': [ ],

    # always loaded
    'data': [
       'views/index.xml',
       'views/movies_list.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'qweb': [
        
    ]
}
