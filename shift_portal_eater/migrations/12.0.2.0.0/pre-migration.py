import logging

from openupgradelib import openupgrade

_logger = logging.getLogger(__name__ + " 12.0.2.0.0")


renamed_view_xml_ids = (
    (
        "beesdoo_website_eater.beesdoo_website_eater_templates",
        "shift_portal_eater.shift_portal_eater_templates",
    ),
)


@openupgrade.migrate()
def migrate(env, version):
    _logger.info("renaming view xml ids")
    openupgrade.rename_xmlids(env.cr, renamed_view_xml_ids)
