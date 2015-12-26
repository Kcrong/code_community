#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import render_template, redirect, url_for, request

from . import article_blueprint


@article_blueprint.route('/write')
def article_write():
    return render_template('article/write.html')