""" Production Settings """
# default: use settings from main settings.py if not overwritten
from .settings import *

import django_heroku


DEBUG = False
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', SECRET_KEY)
ALLOWED_HOSTS = ['phil-dan.herokuapp.com']

# Activate Django-Heroku.
django_heroku.settings(locals())

