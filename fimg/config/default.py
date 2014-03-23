from os.path import dirname, normpath, join
CONFIG_DIR = normpath(dirname(__file__))
PROJ_ROOT = dirname(dirname(CONFIG_DIR))

SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
SQLALCHEMY_ECHO = False
DEBUG = True

DATE_FORMAT = "%Y-%m-%d"
TIME_FORMAT = "%H:%M:%S"
DATETIME_FORMAT = DATE_FORMAT+" "+TIME_FORMAT

TUMBLR = {
    'key':'gvJPyLg57Wgu1ivg0kP2tc2KBk9o57qOCQJgwcFJVbrXkXosv8',
    'secret':'b4WpRVEWw1aFoPrfJ7Amp77m7q4tv8p575JHl2RnInsaiZPIy9'
}

INSTAGRAM = {}
