{
    'name': 'Somaya Alasmi Portfolio',
    'summary': 'Bilingual (EN/AR) premium portfolio website for Somaya Alasmi — Data Analyst & Business Intelligence.',
    'description': """
Somaya Alasmi Portfolio
========================
A premium, bilingual (English / Arabic - RTL) personal portfolio website
showcasing Power BI and data analysis projects, built on native Odoo
Website functionality.

Includes:
- Home, Projects, About Me and Contact pages editable via Website Builder.
- A "Portfolio Project" model powering the Projects listing and individual
  case-study pages, with translatable fields for full EN/AR content.
- Custom premium analytics-inspired styling (navy / charcoal / off-white / mint).
""",
    'version': '17.0.1.0.0',
    'category': 'Website',
    'author': 'Somaya Alasmi',
    'license': 'LGPL-3',
    'depends': ['website', 'base_setup'],
    'data': [
        'security/ir.model.access.csv',
        'data/res_company_data.xml',
        'data/portfolio_project_data.xml',
        'data/portfolio_project_data_ar.xml',
        'data/website_menu_data.xml',
        'views/portfolio_project_views.xml',
        'views/website_layout.xml',
        'views/page_home.xml',
        'views/page_about.xml',
        'views/page_contact.xml',
        'views/page_projects.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'somaya_portfolio/static/src/scss/portfolio_variables.scss',
            'somaya_portfolio/static/src/scss/portfolio.scss',
            'somaya_portfolio/static/src/js/portfolio.js',
        ],
    },
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': True,
    'post_init_hook': 'post_init_hook',
}
