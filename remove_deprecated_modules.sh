#!/bin/bash

# Usage: remove_deprecated_modules.sh database-name-here
#
# Super simple script that enables less typing.

cd $(dirname "$0")

cat remove_deprecated_modules.py | ~/venv/bin/odoo shell --config ~/odoo.conf --no-http --logfile /dev/stdout --stop-after-init -d $1
