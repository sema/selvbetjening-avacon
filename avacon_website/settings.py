from selvbetjening.settings_base import *

import os
DIRNAME = os.path.abspath(os.path.dirname(__file__))

# email
DEFAULT_FROM_EMAIL = 'noreply@avacon.dk'
SERVER_EMAIL = 'noreply@avacon.dk'

# various settings
ROOT_URLCONF = 'avacon_website.urls'

ADMINS = (
    ('Casper S. Jensen', 'the@sema.dk'),
)

LANGUAGES = (
  ('da-dk', 'Dansk'),
)

MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + (
    'django.middleware.locale.LocaleMiddleware',
)

# template directories
TEMPLATE_DIRS = [
    os.path.join(DIRNAME, 'templates')
] + TEMPLATE_DIRS

STATICFILES_DIRS = (
    os.path.join(DIRNAME, 'static'),
)

# installed applications
INSTALLED_APPS.extend([
    'django_extensions',
    'django.contrib.webdesign',

    'selvbetjening.viewbase.forms',
    'selvbetjening.viewbase.copyright',

    'selvbetjening.portal.quickregistration',
    'selvbetjening.portal.profile',
    'selvbetjening.portal.eventregistration',

    'avacon_website.apps.simpleregistration',

    'selvbetjening.sadmin.base',
    'selvbetjening.sadmin.members',
    'selvbetjening.sadmin.events',
    'selvbetjening.sadmin.mailcenter',
])

# SVS SPECIFIC

LOGIN_REDIRECT_URL = '/min-oversigt/'

LOGIN_URL = '/sadmin/'

AVACON_EVENT_ID = 1

try:
    from settings_local import *
except ImportError:
    pass
