# main application entry
import os
import sys
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object('fimg.config.default')

#silly
for a in sys.argv:
    if 'test' in a:
        print "I see you test something here, so I'll use test DB in memory"
        app.config.from_pyfile(os.path.join(app.config['CONFIG_DIR'],'test.cfg'))
        break

env = os.environ.get('FIMG_CONFIG')
if env:
    app.config.from_envvar('FIMG_CONFIG')


app.url_map.strict_slashes = False

db = SQLAlchemy(app)


#import all models
from fimg.models import *
