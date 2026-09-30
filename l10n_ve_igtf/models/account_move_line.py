from odoo import fields, models


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    display_type = fields.Selection(
        selection_add=[("l10n_ve_igtf", "IGTF")],
        ondelete={"l10n_ve_igtf": "set rounding"},
    )

    def _l10n_ve_assign_company_default_tax_if_empty(self):
        self.ensure_one()
        if self.move_id.l10n_ve_igtf_surplus_credit_note:
            return
        return super()._l10n_ve_assign_company_default_tax_if_empty()

    def _put_unique_tax_per_line(self):
        self.ensure_one()
        if self.move_id.l10n_ve_igtf_surplus_credit_note:
            return
        return super()._put_unique_tax_per_line()
