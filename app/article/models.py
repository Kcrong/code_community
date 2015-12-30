#!/usr/bin/env python
# -*- coding:utf-8 -*-

from .. import db
from ..user.models import Users


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30))
    code = db.Column(db.Text)
    content = db.Column(db.Text)
    answer = db.relationship('Answer', lazy='dynamic', backref='Article')
    writer = db.Column(db.Integer, db.ForeignKey('users.id'))
    tag = db.relationship('Tag', lazy='dynamic', backref='Article')

    def __init__(self, title, code, content, writer):
        self.title = title
        self.code = code
        self.content = content
        self.writer = writer


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    article = db.Column(db.Integer, db.ForeignKey('article.id'))
    content = db.Column(db.Text)
    writer = db.Column(db.Integer, db.ForeignKey('users.id'))
    like = db.Column(db.Integer, default=0)

    def __init__(self, article, content, writer):
        self.article = article
        self.writer = writer
        self.content = content


class Answer_like(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    answer = db.Column(db.Integer)
    user = db.Column(db.Integer)

    def __init__(self, answer, user):
        self.answer = answer
        self.user = user


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    article = db.Column(db.Integer, db.ForeignKey('article.id'))
    content = db.Column(db.String(30))

    def __init__(self, article, content):
        self.article = article
        self.content = content
