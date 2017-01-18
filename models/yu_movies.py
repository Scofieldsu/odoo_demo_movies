# -*- coding: utf-8 -*-
# author : scofield.yu

from odoo import api, fields, models
from odoo.exceptions import ValidationError

class YuMovies(models.Model):
    _name = 'yu.movies'

    name = fields.Char(string='电影名称')
    director = fields.Char(string='导演')
    show_date = fields.Date(string='上映时间')
    area = fields.Char(string='地区')
    style = fields.Char(string='类型')
    score = fields.Float(string='评分')
    summary = fields.Text(string='简介')
    your_actions = fields.Char(string='关于电影,你')
    liked = fields.Boolean(string='喜欢')
    watched = fields.Boolean(string='已看过')
    planed = fields.Boolean(string='计划看')
    film_critic = fields.Text(string='影评')