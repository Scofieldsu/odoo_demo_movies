# -*- coding: utf-8 -*-
# author : scofield.yu

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class YuArea(models.Model):
    _name = 'yu.area'

    name = fields.Char(string='地区')
    area_movies = fields.One2many(
        'yu.area.movies.line',
        'yu_area_id',
        string='地区电影列表',
        copy=True
    )

class YuAreaMoviesList(models.Model):
    _name = 'yu.area.movies.line'

    yu_area_id = fields.Many2one(
        'yu.area',
        string='地区id',
        required=True,
        ondelete='cascade',
        index=True,
        copy=False
    	)
    movies_id = fields.Many2one(
        string='电影名称',
        comodel_name='yu.movies',

        )
    directors= fields.Many2many(string='导演',related='movies_id.directors')
    # actors = fields.Many2many(string='演员',related='movies_id.actors')
    show_date = fields.Date(string='上映时间',related='movies_id.show_date')
    area_id = fields.Many2one(string='地区',related='movies_id.area_id')
    style_ids = fields.Many2many(string='类型',related='movies_id.style_ids')
    score = fields.Float(string='评分(10分制)',related='movies_id.score')
