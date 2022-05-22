import datetime
from pathlib import Path
import os, sys, json

from setup import env

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = os.environ['DEBUG']
ALLOWED_HOSTS = json.loads(os.environ['ALLOWED_HOSTS'])

# LOGGING_CONFIG = None

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    # third party apps
    'cloudinary_storage',
    'cloudinary',
    'rest_framework',
    'django_filters',
    'corsheaders',
    'rangefilter',
    #oauth
    'rest_framework.authtoken',
    'rest_auth',
    'allauth',
    'allauth.account',
    'rest_auth.registration',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    # my apps
    'omnistack6',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'setup.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'setup.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

# time zone and language
LANGUAGE_CODE = os.environ['LANGUAGE_CODE']
TIME_ZONE = os.environ['TIME_ZONE']
USE_I18N = True
USE_L10N = True
USE_TZ = True

# static and media
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'
STATICFILES_DIRS = [ 'setup/static' ]
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media/'
BASE_URL = os.environ['BASE_URL']

USE_CLOUDINARY = os.environ['CLOUDINARY']
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ['CLOUD_NAME'],
    'API_KEY': os.environ['API_KEY'],
    'API_SECRET': os.environ['API_SECRET'],
}
if USE_CLOUDINARY:
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# apps folder
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

# api configuration
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
    'DEFAULT_THROTTLE_RATES': {
        'user': '1000/day'
    }
}
REST_USE_JWT = True

# CORS
CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = json.loads(os.environ['CORS_ALLOWED_ORIGINS'])

# locale
LOCALE_PATHS = [ BASE_DIR, 'locale' ]

# OAUTH
SITE_ID = 2

# JWT
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=3600),
}
