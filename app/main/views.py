#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import render_template, session, request
from sqlalchemy import desc
from werkzeug.exceptions import BadRequestKeyError
from . import main_blueprint
from .. import db
from ..article.models import Article
from ..article.models import Tag


@main_blueprint.route('/')
def index():
    try:
        login = session['login']
    except KeyError:
        session['login'] = False

    try:
        tag = request.args['tag']
    except BadRequestKeyError:

        db_data = db.session.query(Article).order_by(desc(Article.id)).all()

    else:
        all_tag = db.session.query(Tag).filter_by(content=tag).all()
        articles = []
        for tag in all_tag:
            articles.append(tag.article)

        articles = set(articles)
        db_data = []
        for article in articles:
            for i in db.session.query(Article).filter_by(id=article).all():
                db_data.append(i)

    tag_data = {}
    for article in db_data:
        tags = db.session.query(Tag).filter_by(article=article.id).all()
        tag_data[article.id] = tags

    return render_template('main/index.html',
                           Alldata=db_data,
                           userdata=session,
                           login=login,
                           tag_data=tag_data
                           )
