# -*- coding: utf-8 -*-
# author : scofield.yu

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class YuDirector(models.Model):
    _name = 'yu.director'

    name = fields.Char(string='导演')
    area_id = fields.Many2one('yu.area', ondelete='restrict',string='地区')
    birthdate = fields.Date(string="出生日期")
    director_movies = fields.One2many(
        'yu.director.movies.line',
        'yu_director_id',
        string='导演电影',
        copy=True
    )

    director_awards = fields.One2many(
        'yu.director.awards',
        'yu_director_id',
        string='获奖情况',
        copy=True
    )

class YuDirectorMoviesList(models.Model):
    _name = 'yu.director.movies.line'

    yu_director_id = fields.Many2one(
        'yu.director',
        string='导演id',
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

class YuDirectorAwards(models.Model):
    _name = 'yu.director.awards'
    
    yu_director_id = fields.Many2one(
        'yu.director',
        string='获奖情况',
        required=True,
        ondelete='cascade',
        index=True,
        copy=False
    )
    # 哪一届？什么奖？
    movies_awards_id = fields.Many2one('yu.awards',string='电影奖',ondelete='restrict')
    # 1部电影多个奖项？
    awards_type_id = fields.Many2one('yu.awards.type',string='奖项',ondelete='restrict')

    awards = fields.Selection(
        string='获奖／提名',
        selection='_get_movie_awards',
    ) 
    movies_id = fields.Many2one(
	    string='获奖电影',
	    comodel_name='yu.movies',)
    @api.model
    def _get_movie_awards(self):
        return [
            ('1', '🏆'),
            ('0', '提名')
        ]
