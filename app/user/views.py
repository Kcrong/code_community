#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import render_template, redirect, url_for, request

from . import user_blueprint


@user_blueprint.route('/')
def user_main():
    return redirect(url_for('user.user_login'))


@user_blueprint.route('/login')
def user_login():
    return render_template('user/login.html')


@user_blueprint.route('/signup', methods=['GET', 'POST'])
def user_signup():
    if request.method == 'GET':
        return render_template('user/signup.html')
    else:
        data = request.form
        # [('job', u'1'), ('nickname', u'kcrong'), ('password', u'rlagusdn'), ('userid', u'hyunwoo1010'), ('email', u'kcrong@kim82536.pe.kr')


        return render_template('user/signup.html')


@user_blueprint.route('/home')
def user_home():
    return render_template('user/home.html')
