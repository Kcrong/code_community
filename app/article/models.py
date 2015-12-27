#!/usr/bin/env python
# -*- coding:utf-8 -*-

from .. import db


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30))
    code = db.Column(db.String(1000))
    content = db.Column(db.String(500))
    answer = db.relationship('Answer', lazy='dynamic', backref='Article')
    writer = db.Column(db.String(20))

    def __init__(self, title, code, content, writer):
        self.title = title
        self.code = code
        self.content = content
        self.writer = writer


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    article = db.Column(db.Integer, db.ForeignKey('article.id'))
    content = db.Column(db.String(500))
    writer = db.Column(db.Integer)

    def __init__(self, article, content, writer):
        self.article = article
        self.writer = writer
        self.content = content
