# -*- coding: utf-8 -*-
# author : scofield.yu

from odoo import api, fields, models
from odoo.exceptions import ValidationError

class YuMovies(models.Model):
    _name = 'yu.movies'

    name = fields.Char(string='电影名称')
    # 1部电影多个导演？
    directors= fields.Many2many('yu.director','yu_movies_director_rel','movies_id','directors',string='导演')
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
    film_awards = fields.One2many(
        'yu.movies.awards',
        'yu_movies_id',
        string='获奖情况',
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

    @api.multi
    def _check_movies_types(self):
        sql="""select id,area_id from yu_movies"""
        self.env.cr.execute(sql)
        fet=self.env.cr.dictfetchall()
        if not fet:
            return True
        else:
            for movie in fet:
                movie_id=movie['id']
                area_id=movie['area_id']
                self.env.cr.execute("""select id from yu_area_movies_line where movies_id=%s""",(movie_id,))
                area_fet=self.env.cr.dictfetchall()
                if area_fet:
                    pass
                else:
                    self.env.cr.execute("""insert into yu_area_movies_line (yu_area_id,movies_id) values (%s,%s)""",(area_id,movie_id))

        

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

class YuMoviesAwards(models.Model):
    _name = 'yu.movies.awards'
    
    yu_movies_id = fields.Many2one(
        'yu.movies',
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

    @api.model
    def _get_movie_awards(self):
        return [
            ('1', '🏆'),
            ('0', '提名')
        ]
