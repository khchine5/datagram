from .base import *

DEBUG = True
ALLOWED_HOSTS = ['khchine5.pythonanywhere.com']
CORS_ORIGIN_ALLOW_ALL = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'dbprod.sqlite3',
    }
}
