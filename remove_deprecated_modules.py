# Post-migration script
#
# This script should be run on the database in version 12.0 after the
# migration process.
#
# Run this script like this:
#   cat thisfile.py | ./odoo/odoo-bin shell -c odoo12.conf -d dbname --no-http --stop-after-init

import logging

_logger = logging.getLogger(__name__)

#
# Update App list
# ===============
self.env["ir.module.module"].update_list()

#
# Remove modules
# ==============
modules_to_uninstall = [
    "beesdoo_account",
]
for module in modules_to_uninstall:
    _logger.info("uninstall %s" % module)
    try:
        self.env["ir.module.module"].search(
            [("name", "=", module)]
        ).button_immediate_uninstall()
    except odoo.exceptions.UserError as err:
        print(err)

self.env.cr.commit()
