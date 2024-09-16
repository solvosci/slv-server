# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)


from odoo import fields, models


class ResUsers(models.Model):
    _inherit = "res.users"

    unrestrict_fields = fields.Boolean(string="Don't restrict fields", compute="_compute_unrestrict_fields")

    def _compute_unrestrict_fields(self):
        has_group = self.env.user.has_group("base_restrict_user_fields.group_user_mgmt_unrestrict_fields")
        for user in self:
            user.unrestrict_fields = has_group
