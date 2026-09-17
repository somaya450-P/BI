import re

from odoo import fields, models

TOOL_SEPARATOR_RE = re.compile(r'[,،]')


class PortfolioProject(models.Model):
    _name = 'portfolio.project'
    _description = 'Portfolio Project'
    _order = 'sequence, id'
    _rec_name = 'name'

    active = fields.Boolean(default=True)
    sequence = fields.Integer(default=10)
    number = fields.Char(string='Project Number', help='e.g. 01, 02...')

    name = fields.Char(string='Title', translate=True, required=True)
    subtitle = fields.Char(string='Subtitle', translate=True)
    overview = fields.Text(string='Overview', translate=True)
    key_analysis = fields.Html(string='Key Analysis', translate=True, sanitize=False)
    highlights = fields.Html(string='Dashboard Highlights', translate=True, sanitize=False)
    tools = fields.Char(string='Tools & Techniques', translate=True,
                         help='Comma-separated list of tool/technique tags.')

    dashboard_url = fields.Char(string='Interactive Dashboard URL (Power BI)')
    linkedin_url = fields.Char(string='LinkedIn Post URL')

    cover_image = fields.Image(string='Cover Image', max_width=1920, max_height=1920)
    image_2 = fields.Image(string='Additional Image 2', max_width=1920, max_height=1920)
    image_3 = fields.Image(string='Additional Image 3', max_width=1920, max_height=1920)

    cover_placeholder = fields.Char(string='Cover Placeholder Path')
    image_2_placeholder = fields.Char(string='Image 2 Placeholder Path')
    image_3_placeholder = fields.Char(string='Image 3 Placeholder Path')

    def tool_list(self):
        self.ensure_one()
        return [t.strip() for t in TOOL_SEPARATOR_RE.split(self.tools or '') if t.strip()]
