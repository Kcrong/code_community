#!/usr/bin/env python
# -*- coding:utf-8 -*-

from .. import db


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30))
    code = db.Column(db.String(1000))
    content = db.Column(db.String(500))

    def __init__(self, title, code, content):
        self.title = title
        self.code = code
        self.content = content
