#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import render_template, session
from sqlalchemy import desc

from . import main_blueprint
from .. import db
from ..article.models import Article


@main_blueprint.route('/')
def index():
    try:
        login = session['login']
    except KeyError:
        login = False
        userdata = None
    else:
        if session['login']:
            userdata = session
        else:
            userdata = None

    db_data = db.session.query(Article).order_by(desc(Article.id)).all()

    return render_template('main/index.html',
                           Alldata=db_data,
                           userdata=userdata,
                           login=login
                           )
