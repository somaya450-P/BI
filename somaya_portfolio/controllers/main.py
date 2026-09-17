from odoo import http
from odoo.http import request


class PortfolioController(http.Controller):

    @http.route(['/projects'], type='http', auth='public', website=True, sitemap=True)
    def portfolio_projects(self, **kwargs):
        projects = request.env['portfolio.project'].sudo().search([], order='sequence, id')
        values = {
            'projects': projects,
        }
        return request.render('somaya_portfolio.page_projects_list', values)

    @http.route(['/projects/<model("portfolio.project"):project>'],
                type='http', auth='public', website=True, sitemap=True)
    def portfolio_project_detail(self, project, **kwargs):
        projects = request.env['portfolio.project'].sudo().search([], order='sequence, id')
        current_index = list(projects.ids).index(project.id) if project.id in projects.ids else -1
        next_project = False
        if current_index != -1 and len(projects) > 1:
            next_project = projects[(current_index + 1) % len(projects)]
        values = {
            'project': project,
            'projects': projects,
            'next_project': next_project,
        }
        return request.render('somaya_portfolio.page_project_detail', values)
