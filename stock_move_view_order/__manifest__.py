# -*- coding: utf-8 -*-
{
    'name': "stock_move_view_order",

    'author': 'Polln group',

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'website': "https://github.com/beescoop/Obeesdo",
    'licence': "AGPL-3",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Extra tools', # HERE
    'version': '12.0.2.1.0',

    'sequence': '10',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock'],

    # always loaded
    'data': [
        "views/inhereted_view_from_stock_move_line.xml"
        # 'security/ir.model.access.csv',
    ],
    "installable": True,
    "application": True,
    "auto_install": False
}
