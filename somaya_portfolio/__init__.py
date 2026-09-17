from . import models
from . import controllers

from odoo import api, SUPERUSER_ID


def post_init_hook(cr, registry):
    """Activate Arabic on the website and set the company identity."""
    env = api.Environment(cr, SUPERUSER_ID, {})

    ar_lang = env['res.lang'].search([('code', 'in', ('ar_001', 'ar_SA'))], limit=1)
    if not ar_lang:
        for code in ('ar_001', 'ar_SA'):
            try:
                env['res.lang']._activate_lang(code)
                ar_lang = env['res.lang'].search([('code', '=', code)], limit=1)
                if ar_lang:
                    break
            except Exception:
                continue

    website = env['website'].search([], limit=1)
    if website:
        en_lang = env.ref('base.lang_en', raise_if_not_found=False)
        lang_ids = website.language_ids.ids
        if en_lang and en_lang.id not in lang_ids:
            lang_ids.append(en_lang.id)
        if ar_lang and ar_lang.id not in lang_ids:
            lang_ids.append(ar_lang.id)
        vals = {'language_ids': [(6, 0, lang_ids)]}
        if en_lang:
            vals['default_lang_id'] = en_lang.id
        website.write(vals)
