# -*- coding: utf-8 -*-
# author : scofield.yu

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class YuArea(models.Model):
    _name = 'yu.area'

    name = fields.Char(string='地区')