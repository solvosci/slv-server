# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See https://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Restrict User Fields",
    "summary": """
        Restricts editing of sensitive fields in res.users.
    """,
    "version": "13.0.1.0.0",
    "license": "LGPL-3",
    "category": "Base",
    "author": "Solvos",
    "website": "https://github.com/solvosci/slv-server",
    "depends": [
        "base",
    ],
    "data": [
        'security/base_restrict_user_fields.xml',
        'views/res_users_views.xml',
    ],
}
