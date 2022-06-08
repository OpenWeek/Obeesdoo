# Copyright 2017 - 2020 BEES coop SCRLfs
#   - Elouan Lebars <elouan@coopiteasy.be>
#   - Rémy Taymans <remy@coopiteasy.be>
#   - Houssine BAKKALI <houssine@coopiteasy.be>
#   - Manuel Claeys Bouuaert <manuel@coopiteasy.be>
#   - Vincent Van Rossem <vincent@coopiteasy.be>
#   - Elise Dupont
#   - Thibault François
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "beesdoo_product",
    "summary": """
        Modification of product module for the needs of beescoop
        """,
    "author": "Beescoop - Cellule IT, Coop IT Easy SCRLfs",
    "website": "https://github.com/beescoop/Obeesdoo",
    "category": "Sales",
    "version": "12.0.2.0.0",
    "depends": [
        "product",
        "sale",
        "point_of_sale",
        "purchase",
        "product_main_supplier",
        "sale_suggested_price",
    ],
    "data": [
        "data/product_label.xml",
        "data/product_hazard.xml",
        "data/barcode_rule.xml",
        "data/product_sequence.xml",
        "views/beesdoo_product.xml",
        "views/assets.xml",
        "wizard/views/label_printing_utils.xml",
        "security/ir.model.access.csv",
    ],
    "installable": True,
    "license": "AGPL-3",
}
