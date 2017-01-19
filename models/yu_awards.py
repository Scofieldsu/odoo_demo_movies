# -*- coding: utf-8 -*-
# author : scofield.yu

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class YuAwards(models.Model):
    _name = 'yu.awards'

    name=fields.Char(string='电影奖')

class YuAwardsType(models.Model):
    _name = 'yu.awards.type'

    name=fields.Char(string='奖项')