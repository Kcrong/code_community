#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask, send_from_directory
from flask.ext.sqlalchemy import SQLAlchemy


def create_app():
    app = Flask(__name__)

    from main import main_blueprint
    from user import user_blueprint
    from article import article_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(user_blueprint, url_prefix='/user')
    app.register_blueprint(article_blueprint, url_prefix='/article')
    return app


app = create_app()
db = SQLAlchemy(app).init_app(app)


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
