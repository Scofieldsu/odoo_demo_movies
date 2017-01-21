# -*- coding: utf-8 -*-
# author : scofield.yu

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class YuActor(models.Model):
    _name = 'yu.actor'

    name = fields.Char(string='演员')
    area_id = fields.Many2one('yu.area', ondelete='restrict',string='地区')
    birthdate = fields.Date(string="出生日期")