from os.path import dirname, normpath, join
CONFIG_DIR = normpath(dirname(__file__))
PROJ_ROOT = dirname(dirname(CONFIG_DIR))

SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
SQLALCHEMY_ECHO = False
DEBUG = True

DATE_FORMAT = "%Y-%m-%d"
TIME_FORMAT = "%H:%M:%S"
DATETIME_FORMAT = DATE_FORMAT+" "+TIME_FORMAT

#set up proper values in local.py
TUMBLR = {
    'key':'',
    'secret':'',
    'token':'',
    'token_secret':''
}

INSTAGRAM = {
    'token':'',
    'id':'',
    'secret':''
}
try:
    from .local import *
except ImportError:
    print "Could not load local settings"
