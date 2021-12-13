import os

is_debug = os.environ.get('DEBUG', 'False').lower() == 'true'


class BaseConfig(object):
    SECRET_KEY = os.environ['SECRET_KEY']
    DEBUG = is_debug
    BOOTSTRAP_SERVE_LOCAL = True
    FLASK_ENV = 'development' if is_debug else 'production'
