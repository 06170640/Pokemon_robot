from .settings import *

import dj_database_url
DATABASES = {
    'default': dj_database_url.config(),
}

STATIC_ROOT = 'static'
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
ALLOWED_HOSTS = ['*']
DEBUG = False



