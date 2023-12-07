# -*- coding: utf-8 -*-
{
    'name': "openacademy",
    "version": "15.0.1",
    'sequence': -100,

    "author": "alaa/",
    "license": "AGPL-3",
    "website": "https://alaa.my/",

    #'category': 'Accounting & Finance',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail',],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/Courses.xml',
    ],

    'installable': True,
    'application': True,
    'auto_install': False,

}
