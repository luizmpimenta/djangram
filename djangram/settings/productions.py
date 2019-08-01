from djangram.settings.base import *
import django_heroku
from decouple import config

SECRET_KEY = config('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = [
    '.herokuapp.com',
]

# ID do Cliente
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = config('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = config('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET')
# EMAIL
EMAIL_HOST_USER = config('EMAIL_HOST_USER',default='')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD',default='')


django_heroku.settings(locals())
