# Copyright 2022 Coop IT Easy SCRLfs <http://coopiteasy.be>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Beesdoo Print Label",

    "author": "Polln group",

    "summary": """
    Bring changes at the pdf production of beesdoo_print_category
    """,

    "description": """
    """,

    "version": "12.0.1.1.2",

    "license": "AGPL-3",

    "category": "Sales",

    "author": "Coop IT Easy SCRLfs",

    "website": "https://github.com/beescoop/Obeesdoo",

    "depends": [
        "beesdoo_product",
        "product_print_category",
    ],

    "data": [
        "views/report_pricetag_normal.xml",
        "data/product_print_category.xml",
    ],

    "installable": True,
    "application": True,
    "auto_install": False
}
