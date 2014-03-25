import os
from os.path import dirname, normpath, join
CONFIG_DIR = normpath(dirname(__file__))
PROJ_ROOT = dirname(dirname(CONFIG_DIR))

SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
SQLALCHEMY_ECHO = False
DEBUG = True

DATE_FORMAT = "%Y-%m-%d"
TIME_FORMAT = "%H:%M:%S"
DATETIME_FORMAT = DATE_FORMAT+" "+TIME_FORMAT

#set up proper values in local.py or in env
TUMBLR = {
    'key':os.environ.get('TUMBLR_KEY','' ),
    'secret':os.environ.get('TUMBLR_SECRET','' ),
    'token':os.environ.get('TUMBLR_TOKEN','' ),
    'token_secret':os.environ.get('TUMBLR_TOKEN_SECRET','' )
}

INSTAGRAM = {
    'token':os.environ.get('INSTAGRAM_TOKEN',''),
    'id':os.environ.get('INSTAGRAM_ID',''),
    'secret':os.environ.get('INSTAGRAM_SECRET','')
}
try:
    from .local import *
except ImportError:
    print "Could not load local settings"
