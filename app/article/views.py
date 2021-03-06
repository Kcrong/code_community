#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import render_template, request, redirect, url_for, session

from . import article_blueprint
from .. import db
from models import Article, Answer, Tag, Answer_like
from ..user.models import Users
from sqlalchemy import desc

from werkzeug.exceptions import BadRequestKeyError


@article_blueprint.route('/write', methods=['GET', 'POST'])
def article_write():
    try:
        login = session['login']
    except KeyError:
        session['login'] = False
        return redirect(url_for('user.user_login'))
    else:
        if not login:
            return redirect(url_for('user.user_login'))

    if request.method == 'GET':
        return render_template('article/write.html')

    else:
        data = request.form

        u = db.session.query(Users).filter_by(userid=session['userid']).first()
        article = Article(data['title'], data['code'], data['content'], u.id)
        db.session.add(article)
        db.session.commit()

        tags = data['tag'].split(';')[:4]
        for tag in tags:
            t = Tag(article.id, tag)
            db.session.add(t)
        db.session.commit()

        return redirect(url_for('main.index'))


@article_blueprint.route('/answer', methods=['GET', 'POST'])
def show_answer():
    if request.method == 'GET':
        # all_answer = db.session.query(Answer).filter_by(article=request.args['article']).all()
        #        if all_answer is None:
        #            return ""

        all_answer = []
        all_profile = {}
        all_nickname = {}

        try:
            data = request.args['article']
        except BadRequestKeyError:
            data = 1

        for a, p in db.session.query(Answer, Users).filter(Users.id == Answer.writer).filter(
                        Answer.article == data).order_by(desc(Answer.like)).all():
            all_answer.append(a)
            all_profile[a.writer] = p.profile_img
            all_nickname[a.writer] = p.nickname

        return render_template('article/answer.html',
                               all_answer=all_answer,
                               all_profile=all_profile,
                               all_nickname=all_nickname)
    else:
        try:
            login = session['login']
        except KeyError:
            return redirect(url_for('user.user_login'))
        else:
            if not login:
                return redirect(url_for('user.user_login'))

        data = request.form
        article = db.session.query(Article).filter_by(id=data['article']).first()
        u = db.session.query(Users).filter_by(userid=session['userid']).first()
        answer = Answer(article.id, data['answer'], u.id)

        db.session.add(answer)
        db.session.commit()

        return redirect(url_for('article.show_answer', article=data['article']))


@article_blueprint.route('/add_like', methods=['GET'])
def add_like():
    try:
        login = session['login']
    except KeyError:
        session['login'] = False
        return redirect(url_for('user.user_login'))
    else:
        if not login:
            return redirect(url_for('user.user_login'))

    user = db.session.query(Users).filter_by(userid=session['userid']).first()
    answer = db.session.query(Answer).filter_by(id=request.args['answer']).first()

    if db.session.query(Answer_like).filter_by(answer=answer.id, user=user.id).first() is None:
        pass
    else:
        return render_template('article/error.html', error="Already Liked!")

    db.session.add(Answer_like(answer.id, user.id))
    answer.like += 1
    db.session.commit()

    return redirect(url_for('article.show_answer', article=answer.article))
