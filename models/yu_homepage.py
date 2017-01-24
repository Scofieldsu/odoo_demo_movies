# -*- coding: utf-8 -*-
# author : scofield.yu

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class YuHomepage(models.Model):
    _name = 'yu.homepage'

    name = fields.Char(string='名称',default="个人主页")