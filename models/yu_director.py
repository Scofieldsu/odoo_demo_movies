# -*- coding: utf-8 -*-
# author : scofield.yu

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class YuDirector(models.Model):
    _name = 'yu.director'

    name = fields.Char(string='导演')
    area_id = fields.Many2one('yu.area', ondelete='restrict',string='地区')
    birthdate = fields.Date(string="出生日期")