from .base import *


DEBUG = True
TEMPLATE_DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
INSTALLED_APPS += ('debug_toolbar',)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'insoft_develop',
        'USER': 'insoft',
        'PASSWORD': 'insoft',
        'HOST': 'localhost',
        'CONN_MAX_AGE': 600,
        }
}


try:
    from .local import *
except ImportError:
    pass
