# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See https://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Restrict User Fields",
    "summary": """
        Restricts editing of sensitive fields in res.users.
    """,
    "version": "17.0.1.0.0",
    "license": "LGPL-3",
    "category": "Base",
    "author": "Solvos",
    "website": "https://github.com/solvosci/slv-server",
    "data": [
        'security/base_restrict_user_fields.xml',
        'views/res_users_views.xml',
    ],
}
