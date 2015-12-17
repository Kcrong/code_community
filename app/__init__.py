#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask, send_from_directory

app = Flask(__name__)


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


def create_app():
    from main import main_blueprint
    app.register_blueprint(main_blueprint)
    return app
