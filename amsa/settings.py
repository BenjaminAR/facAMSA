"""

Using Django 3.2.9.

"""

from pathlib import Path
import os
from decouple import config
from django.contrib.messages import constants as msj_error

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'apps.app_autenticacion',
    'apps.app_factura',
    'apps.app_dashboard',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'amsa.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'amsa.wsgi.application'

#DATABASES = config('databases')


DATABASES = {

    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':'AMSA',
        'USER':'postgres',
        'PASSWORD':'123456',
        'HOST':'localhost',
        'PORT': 5432,
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'es-mx'

USE_TZ = True

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True




STATIC_URL = '/static/'
STATIC_MEDIA ='/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media'),

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LOGIN_REDIRECT_URL = '/factura/index'
LOGOUT_REDIRECT_URL ='/login'
LOGIN_URL='/login' 

MESSAGAE_TAGS={

    msj_error.DEBUG: 'debug',
    msj_error.INFO: 'info',
    msj_error.SUCCESS: 'success',
    msj_error.WARNING: 'warning',
    msj_error.ERROR: 'danger',

}

CRISPY_TEMPLATE_PACK = 'bootstrap4'