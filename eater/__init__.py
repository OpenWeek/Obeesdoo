from . import models
from . import wizard


from openupgradelib import openupgrade
from odoo import api, SUPERUSER_ID


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


def rename_xml_ids(cr):
    env = api.Environment(cr, SUPERUSER_ID, {})

    openupgrade.rename_xmlids(env.cr, renamed_view_xml_ids)
