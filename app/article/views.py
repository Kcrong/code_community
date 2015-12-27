#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import render_template, request, redirect, url_for

from . import article_blueprint
from .. import db
from models import Article


@article_blueprint.route('/write', methods=['GET', 'POST'])
def article_write():

    if request.method == 'GET':
        return render_template('article/write.html')

    else:
        data = request.form
        article = Article(data['title'], data['code'], data['content'])
        db.session.add(article)
        db.session.commit()

        return redirect(url_for('main.index'))

