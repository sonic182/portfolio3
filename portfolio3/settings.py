"""
Django settings for portfolio3 project.

Generated by 'django-admin startproject' using Django 1.10.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

import dj_database_url

from django.utils.translation import ugettext_lazy as _

environ = os.environ
env = environ.get('PYTHON_ENV') or 'development'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

if env == 'production':
    EMAIL_HOST = environ.get('EMAIL_HOST')
    EMAIL_HOST_USER = environ.get('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = environ.get('EMAIL_HOST_PASSWORD')
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True

    SECRET_KEY = environ.get('SECRET_KEY')
    DEBUG = False
elif env == 'test':
    SECRET_KEY = '+v%(ju0tm#(qg8g0a+kcjkn#6$9tt8qbue3^ces^w$qqikhj=l'
    DEBUG = True
else:  # development
    # mailcatcher
    EMAIL_HOST = '127.0.0.1'
    EMAIL_HOST_USER = ''
    EMAIL_HOST_PASSWORD = ''
    EMAIL_PORT = 1025
    EMAIL_USE_TLS = False

    SECRET_KEY = '+v%(ju0tm#(qg8g0a+kcjkn#6$9tt8qbue3^ces^w$qqikhj=l'
    DEBUG = True


ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    # third parts apps
    'ckeditor',
    'ckeditor_uploader',
    'widget_tweaks',
    'pipeline',
    # my apps
    'home',
    'courses',
]

# must be MIDDLEWARE but just for compatibility...
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.gzip.GZipMiddleware',

    'pipeline.middleware.MinifyHTMLMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware'
]

ROOT_URLCONF = 'portfolio3.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join('templates')],
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

WSGI_APPLICATION = 'portfolio3.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

if env == 'production':
    DATABASES = {}
    DATABASES['default'] = dj_database_url.config(conn_max_age=600)
    # DATABASES = {
    #     'default': {
    #         'ENGINE': 'django.db.backends.sqlite3',
    #         'NAME': os.path.join(BASE_DIR, 'db/production.sqlite3'),
    #     }
    # }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db/db.sqlite3'),
        }
    }


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# I18n
LANGUAGES = [
    ('es', _('Spanish')),
    ('en', _('English')),
]

LOCALE_PATHS = (
    os.path.join(BASE_DIR, "locale"),
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = environ.get('STATIC_URL') or '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    os.path.join(BASE_DIR, "assets"),
    # os.path.join(BASE_DIR, "node_modules"),
]
STATIC_ROOT = os.path.join(BASE_DIR, "public/static")

MEDIA_URL = environ.get('MEDIA_URL') or '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "public/media")

# CKEDITOR
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'
CKEDITOR_UPLOAD_PATH = "ckeditor_uploads/"
CKEDITOR_IMAGE_BACKEND = 'pillow'

# PIPELINE

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)

PIPELINE = {
    'ENABLED': True,
    'YUGLIFY_BINARY': "{base}/node_modules/.bin/yuglify".format(base=BASE_DIR)
}

PIPELINE['STYLESHEETS'] = {
    'home': {
        'source_filenames': (
            'scss/app.scss',
        ),
        'output_filename': 'css/main.css',
        'extra_context': {
            'media': 'screen,projection',
        },
    },
}


# PIPELINE['JAVASCRIPT'] = {
#   'homee': {
#     'source_filenames': (
#       'js/main.browserify.js',
#     ),
#     'output_filename': 'js/app2.js',
#   },
# }

PIPELINE['COMPILERS'] = (
    'libsasscompiler.LibSassCompiler',
)

# DJANGO SITES
SITE_ID = 1
