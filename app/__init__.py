#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask, send_from_directory
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate

app = Flask(__name__)
db = SQLAlchemy()


def create_app():
    from main import main_blueprint
    from user import user_blueprint
    from article import article_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(user_blueprint, url_prefix='/user')
    app.register_blueprint(article_blueprint, url_prefix='/article')

    app.config.from_pyfile('../config.cfg')
    return app


app = create_app()
db = SQLAlchemy(app).init_app(app)

from article.models import *
from main.models import *
from user.models import *
import article.models
import main.models
import user.models

migrate = Migrate(app, db)


@app.route('/css/<path:filename>')
def css_static(filename):
    return send_from_directory(app.root_path + '/static/css/', filename)


@app.route('/js/<path:filename>')
def js_static(filename):
    return send_from_directory(app.root_path + '/static/js/', filename)


@app.route('/img/<path:filename>')
def img_static(filename):
    return send_from_directory(app.root_path + '/static/img/', filename)


@app.route('/font/<path:filename>')
def font_static(filename):
    return send_from_directory(app.root_path + '/static/font', filename)
