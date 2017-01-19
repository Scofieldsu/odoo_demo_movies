# -*- coding: utf-8 -*-
# author : scofield.yu

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class YuActor(models.Model):
    _name = 'yu.actor'

    name = fields.Char(string='演员')