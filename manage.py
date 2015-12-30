#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask.ext.script import Manager
from app import migrate
from flask.ext.migrate import MigrateCommand
# from werkzeug.contrib.fixers import ProxyFix

from app import app

manager = Manager(app)

manager.add_command('db', MigrateCommand)


@manager.command
def run():
    app.run()


@manager.command
def run_allhost():
    app.run(host='0.0.0.0', port=5000)


if __name__ == "__main__":
    manager.run()
