from .base import *


DEBUG = True
TEMPLATE_DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
INSTALLED_APPS += ('debug_toolbar',)

DATABASES['default']['NAME'] = 'insoft_develop'


try:
    from .local import *
except ImportError:
    pass
