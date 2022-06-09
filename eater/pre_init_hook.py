from openupgradelib import openupgrade

from odoo import SUPERUSER_ID, api


def rename_xml_ids(cr):

    renamed_view_xml_ids = (
        (
            "beesdoo_base.action_eater_wizard",
            "eater.action_eater_wizard",
        ),
        (
            "beesdoo_base.Eater Wizard",
            "eater.Eater Wizard",
        ),
    )
    env = api.Environment(cr, SUPERUSER_ID, {})
    openupgrade.rename_xmlids(env.cr, renamed_view_xml_ids)
