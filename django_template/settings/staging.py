from .base import *

DEBUG = False

INSTALLED_APPS += []

MIDDLEWARE += []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_template',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}

TIME_ZONE = 'UTC'