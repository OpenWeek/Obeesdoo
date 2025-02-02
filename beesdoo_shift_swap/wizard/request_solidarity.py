from datetime import datetime

from odoo import _, api, fields, models
from odoo.exceptions import UserError


class RequestSolidarityShift(models.TransientModel):
    _name = "beesdoo.shift.request.solidarity.shift"
    _description = "Request solidarity shift"

    worker_id = fields.Many2one(
        "res.partner",
        default=lambda self: self.env["res.partner"].browse(
            self._context.get("active_id")
        ),
        required=True,
        string="Cooperator",
        domain=[
            ("is_worker", "=", True),
            ("working_mode", "in", ("regular", "irregular")),
            ("state", "not in", ("unsubscribed", "resigning")),
        ],
    )

    working_mode = fields.Selection(
        related="worker_id.working_mode",
        string="Working mode",
        store=True,
    )

    tmpl_dated_id = fields.Many2one(
        "beesdoo.shift.template.dated",
        string="Shift",
        domain=[
            ("date", ">", datetime.now()),
        ],
    )

    reason = fields.Text(string="Reason", default="")

    def _check(self, group="beesdoo_shift.group_shift_management"):
        self.ensure_one()
        if not self.env.user.has_group(group):
            raise UserError(_("You don't have the required access for this operation."))
        if self.worker_id == self.env.user.partner_id and not self.env.user.has_group(
            "beesdoo_shift.group_cooperative_admin"
        ):
            raise UserError(_("You cannot perform this operation on yourself"))
        return self.with_context(real_uid=self._uid)

    @api.onchange("worker_id")
    def _get_template_dated(self):
        for record in self:
            if record.working_mode == "irregular":
                record.tmpl_dated_id = False
            elif record.working_mode == "regular":
                tmpl_dated_possible = record.worker_id.get_next_tmpl_dated()
                tmpl_dated_wanted = self.env["beesdoo.shift.template.dated"]
                for template in tmpl_dated_possible:
                    tmpl_dated_wanted |= tmpl_dated_wanted.create(
                        {
                            "template_id": template.template_id.id,
                            "date": template.date,
                            "store": False,
                        }
                    )
                return {
                    "domain": {"tmpl_dated_id": [("id", "in", tmpl_dated_wanted.ids)]}
                }

    @api.multi
    def create_request(self):
        self._check()
        data = {
            "worker_id": self.worker_id.id,
            "tmpl_dated_id": self.tmpl_dated_id.id,
            "reason": self.reason,
        }
        self.env["beesdoo.shift.solidarity.request"].sudo().create(data)
