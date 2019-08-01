from djangram.settings.base import *
import django_heroku

SECRET_KEY = 'tu*^paym)n1w^r67-!wu5o$=$kt*tq0jdd#8_^a$n7mw3ga=au'

DEBUG = False

ALLOWED_HOSTS = []

MIDDLEWARE.insert(
    MIDDLEWARE.index('django.middleware.security.SecurityMiddleware') + 1,
    'whitenoise.middleware.WhiteNoiseMiddleware'
)

DATABASES = {

}

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.social_auth.associate_by_email',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)
SOCIAL_AUTH_URL_NAMESPACE = 'social'
AUTHENTICATION_BACKENDS = (
    # Redes Sociais
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.instagram.InstagramOAuth2',

    # Django
    'django.contrib.auth.backends.ModelBackend',
)
# ID do Cliente
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '585280649858-oc85getjf220qfheqe78it9153juhb9i.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'pR91kowfqQfWsO9p1NAuhHZr'
# EMAIL
EMAIL_HOST_USER = 'lmtesteprojetos@gmail.com'
EMAIL_HOST_PASSWORD = 'testeprojetos'

django_heroku.settings(locals())
