# -*- coding: utf-8 -*-
# author : scofield.yu

from odoo import api, fields, models
from odoo.exceptions import ValidationError

class YuAlbum(models.Model):
    _name = 'yu.album'

    name = fields.Char(string='电影专辑')
    introduce = fields.Text(string='专辑简介')
    collection = fields.Boolean(string='收藏')
    album_picture = fields.Html(string='专辑图片')
    album_movies_list = fields.One2many(
        'yu.album.movies.list',
        'yu_album_id',
        string='专辑影片',
        copy=True
    )
    @api.multi
    def action_collection(self):
        self.ensure_one()
        self.write({'collection': 'True'})


class YuAlbumMoviesList(models.Model):
    _name = 'yu.album.movies.list'

    yu_album_id = fields.Many2one(
        'yu.album',
        string='专辑影片',
        required=True,
        ondelete='cascade',
        index=True,
        copy=False
    )

    movies_id = fields.Many2one(
        'yu.movies',
        string='电影名称',
        change_default=True,
        ondelete='restrict'
    	)

    directors= fields.Many2many(string='导演',related='movies_id.directors')
    actors = fields.Many2many(string='演员',related='movies_id.actors')
    show_date = fields.Date(string='上映时间',related='movies_id.show_date')
    area_id = fields.Many2one(string='地区',related='movies_id.area_id')
    style_ids = fields.Many2many(string='类型',related='movies_id.style_ids')
    score = fields.Float(string='评分(10分制)',related='movies_id.score')
    

    