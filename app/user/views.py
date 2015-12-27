#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import render_template, redirect, url_for, request, session
import random
import string

from . import user_blueprint
from .. import static_folder, db

from models import Users

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def randomkey(length):
    return ''.join(random.choice(string.lowercase) for i in range(length))


@user_blueprint.route('/')
def user_main():
    return redirect(url_for('user.user_login'))


@user_blueprint.route('/logout')
def user_logout():
    del (session['profile_img'])
    del (session['nickname'])
    del (session['userid'])
    del (session['email'])
    del (session['job'])

    session['login'] = False

    return redirect(url_for('user.user_login'))


@user_blueprint.route('/login', methods=['GET', 'POST'])
def user_login():
    if request.method == 'GET':

        try:
            login = session['login']
        except KeyError:
            session['login'] = False
            login = session['login']

        return render_template('user/login.html', login=login)

    else:
        data = request.form
        u = db.session.query(Users).filter_by(userid=data['userid'], userpw=data['password']).first()
        if u is None:
            return render_template('user/login.html', error="Wrong ID or PW")
        else:
            session['login'] = True
            session['userid'] = u.userid
            session['nickname'] = u.nickname
            session['profile_img'] = u.profile_img
            session['email'] = u.email
            session['job'] = u.job

            return redirect(url_for('main.index'))


@user_blueprint.route('/signup', methods=['GET', 'POST'])
def user_signup():
    if request.method == 'GET':
        return render_template('user/signup.html',
                               userdata=session)
    else:
        try:
            profile_img = request.files['profile_img']
        except KeyError:
            filename = 'default.jpg'
        else:
            filename = profile_img.filename

            if allowed_file(filename):
                filename = randomkey(len(filename)) + '.' + filename.rsplit('.', 1)[1]
                profile_img.save(static_folder + '/img/profile/' + filename)

            else:
                return render_template('user/signup.html', error="Wrong Profile Image Extension")

        data = request.form

        u = Users(data['userid'], data['password'], data['nickname'], data['email'], data['job'], filename)

        db.session.add(u)
        db.session.commit()

        return redirect(url_for('user.user_login'))


@user_blueprint.route('/home')
def user_home():
    if not session['login']:
        return redirect(url_for('user.user_login'))

    login = True
    userdata = session

    return render_template('user/home.html',
                           login=login,
                           userdata=userdata)
