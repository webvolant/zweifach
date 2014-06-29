# ~*~ coding: utf-8 ~*~

"""
Django settings for devel project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from django.utils.translation import gettext

import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 't9&+m79!3%t)^y4thx-r@1)ke-w7n#*7k03j-se*4qov6upoz%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

INSTALLED_APPS = (
    'localeurl',
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'modeltranslation',
    'pages',
    'bootstrap3',
    'south',
    'orderform',
    'captcha',
    'ckeditor',
    'rosetta',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'localeurl.middleware.LocaleURLMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    

)

LOCALEURL_USE_SESSION = True

ROOT_URLCONF = 'app.urls'

WSGI_APPLICATION = 'app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


#Templates

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'), 
)

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.core.context_processors.i18n',
    'django.contrib.auth.context_processors.auth',
)


LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# эта переменная будет указывать на папку проекта

PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))

# путь до папки media, в общем случае она пуста в начале

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

MEDIA_URL = '/media/'  # URL для медии в шаблонах

#MEDIA_ROOT = '/home/code/webvolant/media/'
#MEDIA_URL = 'http://127.0.0.1:8000/media/'

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')  # пустая папка, сюда будет собирать статику collectstatic

STATIC_URL = '/static/'  # URL для шаблонов


STATICFILES_DIRS = (

    os.path.join(BASE_DIR, 'templates/css'),
)


# "Поисковики" статики. Первый ищет статику в STATICFILES_DIRS,

# второй в папках приложений.

STATICFILES_FINDERS = (

    'django.contrib.staticfiles.finders.FileSystemFinder',

    'django.contrib.staticfiles.finders.AppDirectoriesFinder',

)

REDACTOR_OPTIONS = {'removeStyles': True}

REDACTOR_UPLOAD = 'uploads/'

CKEDITOR_UPLOAD_PATH = ""

#
LANGUAGES = (
    ('de', 'Deutsch'),
    ('ru', 'Russian'),

#    ('en', 'English'),
)

MODELTRANSLATION_DEFAULT_LANGUAGE = 'de'
MODELTRANSLATION_TRANSLATION_REGISTRY = 'zweifach.translation'
#MODELTRANSLATION_LANGUAGES = ('en', 'ru')


EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'volant247@googlemail.com'
EMAIL_HOST_PASSWORD = '9c471de3'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'volant247@googlemail.com'

