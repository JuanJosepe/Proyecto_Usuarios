from .base import *
DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_secret('DB_NAME'),
        'USER': get_secret('USER'),
        'PASSWORD':get_secret('PASSWORD'),
        'HOST':'localhost',
        'PORT':'5432',
    }
}


STATIC_URL = 'static/'


# para llamar los archivos multimedia
MEDIA_URL ='/media/'
