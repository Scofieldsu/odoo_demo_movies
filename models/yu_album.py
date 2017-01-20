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

    @api.multi
    def action_collection(self):
        self.ensure_one()
        self.write({'collection': 'True'})
