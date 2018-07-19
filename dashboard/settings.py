"""
Django settings for dashboard project.

Generated by 'django-admin startproject' using Django 1.9.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
from os import getenv
from os import path
import saml2
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

APPLICATION_DIR = os.path.dirname(globals()['__file__'])

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), ".."),
)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p7zq=2&ms4%&b%5&5^g(ks0%u#^ku%x5z4xc+#(jao+t1h7*n^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ["127.0.0.1", "localhost","dashboard.tl.it.umich.edu"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'dashboard',
    'djangobower',
    'django_nvd3',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)
TEMPLATE_DIRS = (os.path.join(APPLICATION_DIR, 'templates'), )

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(APPLICATION_DIR, 'templates')],
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

ROOT_URLCONF = 'dashboard.urls'

WSGI_APPLICATION = 'dashboard.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'student_dashboard',  # your mysql database name
        'USER': 'student_dashboard_user', # your mysql user for the database
        'PASSWORD': 'student_dashboard_password', # password for user
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}



# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    # os.path.join(PROJECT_ROOT, "static"),
    os.path.join(BASE_DIR, 'bower_components'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
    'djangobower.finders.BowerFinder',
)


# Django-bower
# ------------

# Specifie path to components root (you need to use absolute path)
BOWER_COMPONENTS_ROOT = os.path.join(PROJECT_ROOT, 'components')

#BOWER_PATH = '/usr/local/bin/bower'
BOWER_PATH = '/usr/bin/bower'

BOWER_INSTALLED_APPS = (
    'd3#3.5.5',
    'nvd3#1.7.1',
    'jquery#1.9',
    'underscore',
)

# IMPORT LOCAL SETTINGS
# =====================
try:
    from settings_local import *
except ImportError:
    pass

#Shib

SAML2_URL_PATH = '/accounts/'
# modify to use port request comes
SAML2_URL_BASE = getenv('DJANGO_SAML2_URL_BASE', 'http://localhost:18000/accounts/')

INSTALLED_APPS += ('djangosaml2',)
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'djangosaml2.backends.Saml2Backend',
)
LOGIN_URL = '%slogin/' % SAML2_URL_PATH
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

BASEDIR = path.dirname(path.abspath(__file__))
SAML_CONFIG = {
    'xmlsec_binary': '/usr/bin/xmlsec1',
    'entityid': '%smetadata/' % SAML2_URL_BASE,

    # directory with attribute mapping
    # 'attribute_map_dir': path.join(BASEDIR, 'attribute-maps'),
    'name': 'Ocellus',
    # this block states what services we provide
    'service': {
        # we are just a lonely SP
        'sp': {
            'name': 'Ocellus',
            'name_id_format': ('urn:oasis:names:tc:SAML:2.0:'
                               'nameid-format:transient'),
            'authn_requests_signed': 'true',
            'allow_unsolicited': True,
            'endpoints': {
                # url and binding to the assetion consumer service view
                # do not change the binding or service name
                'assertion_consumer_service': [
                    ('%sacs/' % SAML2_URL_BASE, saml2.BINDING_HTTP_POST),
                ],
                # url and binding to the single logout service view+

                # do not change the binding or service name
                'single_logout_service': [
                    ('%sls/' % SAML2_URL_BASE, saml2.BINDING_HTTP_REDIRECT),
                    ('%sls/post' % SAML2_URL_BASE, saml2.BINDING_HTTP_POST),
                ],
            },

            # attributes that this project need to identify a user
            'required_attributes': ['uid'],

            # attributes that may be useful to have but not required
            'optional_attributes': ['eduPersonAffiliation'],
        },
    },

    # where the remote metadata is stored
    'metadata': {
        'local': [path.join(BASEDIR, 'saml/remote-metadata.xml')],
    },

    # set to 1 to output debugging information
    'debug': 1,

    # certificate
    'key_file': path.join(BASEDIR, 'saml/ocellus-saml.key'),  'cert_file': path.join(BASEDIR, 'saml/ocellus-saml.pem'),
}

ACS_DEFAULT_REDIRECT_URL = getenv('DJANGO_ACS_DEFAULT_REDIRECT', 'http://localhost:18000/')
LOGIN_REDIRECT_URL = getenv('DJANGO_LOGIN_REDIRECT_URL', 'http://localhost:18000/')

SAML_CREATE_UNKNOWN_USER = True

SAML_ATTRIBUTE_MAPPING = {
    'uid': ('username', ),
    'mail': ('email', ),
    'givenName': ('first_name', ),
    'sn': ('last_name', ),
}