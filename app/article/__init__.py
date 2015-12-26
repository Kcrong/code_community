#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Blueprint

article_blueprint = Blueprint('article', __name__)

from . import views