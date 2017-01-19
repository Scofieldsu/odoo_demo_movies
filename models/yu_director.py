# -*- coding: utf-8 -*-
# author : scofield.yu

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class YuDirector(models.Model):
    _name = 'yu.director'

    name = fields.Char(string='导演')