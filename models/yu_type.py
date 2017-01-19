# -*- coding: utf-8 -*-
# author : scofield.yu

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class YuType(models.Model):
    _name = 'yu.type'

    name = fields.Char(string='类型')