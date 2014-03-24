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
    'secret':'b4WpRVEWw1aFoPrfJ7Amp77m7q4tv8p575JHl2RnInsaiZPIy9',
    'token':'xru2BBAvB2tKYcUg7yN4TFTo7gnxpmvXm6IJ3BS136PuJrtHzR',
    'token_secret':'tEkBPu5Hy1dYVgdbHLmZvURe4w97haGF9nYJTKGR75kDlFtlwI'
}

INSTAGRAM = {
    'token':'1204415954.189ac5f.b8aa6ee417da4bb29bd8d1611b9dcbe7',
    'id':'189ac5fae0684e72a2f68d8834d76a15',
    'secret':'ed718569ad364b86a8f72b65c50cee97'
}
