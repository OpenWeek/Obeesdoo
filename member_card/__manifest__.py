# Copyright 2017 - 2020 BEES coop SCRLfs
#   - Robin Keunen <robin@coopiteasy.be>
#   - Houssine bakkali <houssine@coopiteasy.be>
#   - Rémy Taymans <remy@coopiteasy.be>
#   - Elise Dupont
#   - Thibault François
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Member Card",
    "author": "Beescoop - Cellule IT, Coop IT Easy SCRLfs",
    "website": "https://github.com/beescoop/Obeesdoo",
    "category": "Sales",
    "version": "12.0.1.0.1",
    "depends": ["point_of_sale", "purchase", "portal", "partner_firstname"],
    "data": [
        "security/groups.xml",
        "security/ir.model.access.csv",
        "views/partner.xml",
        "wizard/views/member_card.xml",
        "report/beescard.xml",
    ],
    "installable": True,
    "demo": ["demo/cooperators.xml", "demo/eaters.xml"],
    "license": "AGPL-3",
    "pre_init_hook": "rename_xml_ids",
}
