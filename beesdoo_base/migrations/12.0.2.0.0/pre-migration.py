import logging

from openupgradelib import openupgrade

_logger = logging.getLogger(__name__ + " 12.0.2.0.0")


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


@openupgrade.migrate()
def migrate(env, version):
    _logger.info("renaming view xml ids")
    openupgrade.rename_xmlids(env.cr, renamed_view_xml_ids)
