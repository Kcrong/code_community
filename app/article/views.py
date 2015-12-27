#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import render_template, request, redirect, url_for

from . import article_blueprint
from .. import db
from models import Article, Answer


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


@article_blueprint.route('/answer', methods=['GET','POST'])
def show_answer():
    if request.method == 'GET':
        article = db.session.query(Article).filter_by(id=request.args['article']).first()
        all_answer = db.session.query(Answer).filter_by(article=article.id).all()

        return render_template('article/answer.html',
                               all_answer=all_answer)
    else:
        data = request.form

        article = db.session.query(Article).filter_by(id=data['article']).first()

        answer = Answer(article.id, data['answer'], 'tester')

        db.session.add(answer)
        db.session.commit()

        return redirect(url_for('main.index'))


