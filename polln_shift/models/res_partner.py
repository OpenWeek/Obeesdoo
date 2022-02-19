from odoo import api, fields, models, _


class Partner(models.Model):
    _inherit = "res.partner"

    cooperator_type = fields.Selection(string="Cooperator Type", store=True,
        selection="_get_share_type",
        compute="_compute_cooperator_type",
    )
    shift_task_ids = fields.One2many( 'beesdoo.shift.shift', 'worker_id', string="Shifts")

    @api.depends(
        "share_ids",
        "share_ids.share_product_id",
        "share_ids.share_product_id.default_code",
        "share_ids.share_number",
    )
    def _compute_cooperator_type(self):
        for partner in self:
            share_type = ""
            for line in partner.share_ids:
                if line.share_number > 0:
                    share_type = line.share_product_id.default_code
                    break
            partner.cooperator_type = share_type