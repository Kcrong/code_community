#!/usr/bin/env python
# -*- coding:utf-8 -*-

from .. import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.String(30), nullable=False, unique=True)
    userpw = db.Column(db.String(30), nullable=False)
    nickname = db.Column(db.String(30), unique=True)
    email = db.Column(db.String(30), unique=True)
    job = db.Column(db.Integer)
    profile_img = db.Column(db.String(30), unique=True)

    def __init__(self, userid, userpw, nickname, email, job, profile_img):
        self.userid = userid
        self.userpw = userpw
        self.nickname = nickname
        self.email = email
        self.job = job
        self.profile_img = profile_img
