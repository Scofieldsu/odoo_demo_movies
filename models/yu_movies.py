# -*- coding: utf-8 -*-
# author : scofield.yu

from odoo import api, fields, models
from odoo.exceptions import ValidationError

class YuMovies(models.Model):
    _name = 'yu.movies'

    name = fields.Char(string='电影名称')
    director_id= fields.Many2one('yu.director', ondelete='restrict',string='导演')
    actors = fields.Many2many('yu.actor','yu_movies_actor_rel','movies_id','actor_id','演员')
    show_date = fields.Date(string='上映时间')
    area_id = fields.Many2one('yu.area', ondelete='restrict',string='地区')
    style_ids = fields.Many2many('yu.type','yu_movies_type_rel','movies_id','type_id','类型')
    score = fields.Float(string='评分(10分制)')
    summary = fields.Text(string='简介')
    your_actions = fields.Char(string='关于电影,你')
    liked = fields.Boolean(string='喜欢')
    watched = fields.Boolean(string='已看过')
    planed = fields.Boolean(string='计划看')
    film_critic = fields.Text(string='影评')
    poster = fields.Html(string='电影海报')
    film_comments = fields.One2many(
        'yu.movies.comments',
        'yu_movies_id',
        string='大家评论',
        copy=True
    )

    @api.constrains('score')
    def _constrains_score(self):
        if self.score<0:
            raise ValidationError('负分滚粗的垃圾电影～')
        elif self.score>10:
            raise ValidationError('喜欢就是放肆，但爱就是克制!(10分制)')
        else:
        	pass

    @api.multi
    def action_liked(self):
        self.ensure_one()
        self.write({'liked': 'True'})

    @api.multi
    def action_watched(self):
        self.ensure_one()
        self.write({'watched': 'True'})

    @api.multi
    def action_planed(self):
        self.ensure_one()
        self.write({'planed': 'True'})


class YuComments(models.Model):
    _name = 'yu.movies.comments'

    yu_movies_id = fields.Many2one(
        'yu.movies',
        string='大家评论',
        required=True,
        ondelete='cascade',
        index=True,
        copy=False
    )
    # create_uid = Many2one(comodel_name='res.users',
    #     string='评论者',
    #     readonly=True,
    #     default=lambda self: self.env.user.id,)
    comment = fields.Char(string='评论')
    stars = fields.Selection(
        string='评分',
        selection='_get_movie_stars',
    )

    @api.model
    def _get_movie_stars(self):
        return [
            ('1', '🌟'),
            ('2', '🌟🌟'),
            ('3', '🌟🌟🌟'),
            ('4', '🌟🌟🌟🌟'),
            ('5', '🌟🌟🌟🌟🌟'),
        ]
