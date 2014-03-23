from flask.ext.script import Manager
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from fimg import app
from fimg import db

manager = Manager(app)


@manager.command
def syncdb():
    db.create_all()
    print ' + Created db structure'

if __name__ == "__main__":
    manager.run()
