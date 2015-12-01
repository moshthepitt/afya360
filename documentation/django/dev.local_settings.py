import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# sites
SITE_ID = 1

# change the secret key
SECRET_KEY = 'hwokhV3;N5"E\=vV(t&_D@Yxn>CwPpuB=P\Qt8xF#j@E6)Q3:4.:@$+ox[Z!lQR'

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'SOMETHING_SECRET',
        'USER': 'SOMETHING_SECRET',
        'PASSWORD': 'SOMETHING_SECRET',
    }
}

# Emails
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
DEFAULT_FROM_EMAIL = 'Hello World <hello@example.com>'


# static
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
STATIC_ROOT = '/static/'
STATIC_URL = '/static/'

# media
MEDIA_ROOT = '/media/'
MEDIA_URL = '/media/'

# CACHE
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

# DEBUG
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CRISPY_FAIL_SILENTLY = not DEBUG

ALLOWED_HOSTS = []
