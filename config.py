# http://flask.pocoo.org/docs/config/#development-production

import os


class BaseConfig(object):
    # Run `python2 -c 'import os; print os.urandom(24)'`
    # to generate a random key
    # http://flask.pocoo.org/docs/0.10/quickstart/#sessions
    SECRET_KEY = os.environ['SECRET_KEY']
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.environ['UPLOAD_FOLDER']
    CURRENT_YEAR = int(os.environ['CURRENT_YEAR'])
    MAIL_UPDATE_INTERVAL_SECONDS = 60
    HOSTNAME = os.environ['HOSTNAME']
    EMAIL_SUFFIX = os.environ['EMAIL_SUFFIX']


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    BOOTSTRAP_SERVE_LOCAL = True
    MAIL_UPDATE_INTERVAL_SECONDS = 10


class TestingConfig(BaseConfig):
    TESTING = True


class ProductionConfig(BaseConfig):
    pass
