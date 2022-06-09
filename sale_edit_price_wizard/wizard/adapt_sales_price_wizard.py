from odoo import api, fields, models


class AdaptSalesPriceWizard(models.TransientModel):
    _name = "adapt.sales.price.wizard"
    _description = "adapt.sales.price.wizard"

    def _get_selected_products(self):
        return self.env.context["active_ids"]

    product_ids = fields.Many2many("product.template", default=_get_selected_products)

    @api.multi
    def adapt_list_price(self, vals, suggested_price=None):
        self.ensure_one()
        if suggested_price is None:
            suggested_price = self.suggested_price
        vals.setdefault("list_price", suggested_price)

    @api.multi
    def adapt_sales_price(self):
        self.ensure_one()
        for product in self.product_ids:
            vals = {}
            product.adapt_list_price(vals)
            product.write(vals)
