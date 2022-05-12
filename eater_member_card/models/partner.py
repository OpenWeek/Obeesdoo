# Copyright 2020 Coop IT Easy SCRL fs
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class Partner(models.Model):
    _inherit = "res.partner"

    parent_barcode = fields.Char(
        compute="_compute_bar_code", string="Parent Barcode", store=True
    )

    @api.multi
    @api.depends(
        "parent_eater_id",
        "parent_eater_id.barcode",
        "eater",
        "member_card_ids",
    )
    def _compute_bar_code(self):
        for partner in self:
            if partner.eater == "eater":
                partner.parent_barcode = partner.parent_eater_id.barcode
            elif partner.member_card_ids:
                for c in partner.member_card_ids:
                    if c.valid:
                        partner.barcode = c.barcode

    @api.multi
    def _new_eater(self, surname, name, email):
        partner_data = {
            "lastname": name,
            "firstname": surname,
            "customer": True,
            "eater": "eater",
            "parent_eater_id": self.id,
            "email": email,
            "country_id": self.country_id.id,
            "member_card_to_be_printed": True,
        }
        return self.env["res.partner"].create(partner_data)
