"""
Django settings for burger project.

Generated by 'django-admin startproject' using Django 4.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
from environs import Env
import dj_database_url

env = Env()
env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = os.environ.get('SECRET_KEY', '')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG', default=False)

# DEBUG = os.environ.get('DEVELOPMENT')

ALLOWED_HOSTS = ['milestone-four-andrew.herokuapp.com', 'localhost']

# below to deal with csrf stuff
CSRF_TRUSTED_ORIGINS = ['https://*.GITPOD.IO', 'https://*.8000', 'https://milestone-four-andrew.herokuapp.com/']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',  # for creaating the db schema
    'crispy_forms',  # to make forms easier to format using bootstrap
    'django.contrib.sites',  # allauth
    'allauth',  # allauth
    'allauth.account',  # allauth
    'allauth.socialaccount',  # allauth
    'storages',  # for storing static files
    'home',
    'store',
    'cart',
    'checkout',
    'profiles',
    'wishlist',
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

ROOT_URLCONF = 'burger.urls'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'), os.path.join(
                BASE_DIR, 'templates', 'allauth'
                ),
            ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.contexts.cart_contents'
            ],

            # the below done as intent is to use forms throughout whole project.
            # This is from CI Checkout Video 5
            'builtins': [
                'crispy_forms.templatetags.crispy_forms_tags',
                'crispy_forms.templatetags.crispy_forms_field',
            ]
        },
    },
]

# below used because of gitpod. Refer to CI video Toasts - Part 1
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

AUTHENTICATION_BACKENDS = [ 
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1  # allauth

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = 'slaine16@hotmail.com'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True
EMAIL_PORT = 587


ACCOUNT_AUTHENTICATION_METHOD = 'username_email'  # allauth
ACCOUNT_EMAIL_REQUIRED = True  # allauth
ACCOUNT_EMAIL_VERIFICATION = 'none'  # allauth
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True  # allauth
ACCOUNT_USERNAME_MIN_LENGTH = 4  # allauth
LOGIN_URL = '/accounts/login/'  # allauth
LOGIN_REDIRECT_URL = '/'  # allauth

WSGI_APPLICATION = 'burger.wsgi.application'

# below for the db schema
GRAPH_MODELS = {
  'all_applications': True,
  'group_models': True,
  "app_labels": [
        'home',
        'store',
        'cart',
        'checkout',
        'profiles',
        'wishlist',
        ],
}

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases


if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse('postgres://qeewwjcokmpenn:4e65b80e4a2a09309d6f6b9c872129ada4e9d3ba904168194dc35b9e777cf677@ec2-52-51-155-48.eu-west-1.compute.amazonaws.com:5432/dau2efrl3sabag')
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }



# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL = '/media/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

# the below makes it so images added through the admin panel go to and are accessed from static/images
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/media')
# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STRIPE_CURRENCY = 'GBP'
STRIPE_WH_SECRET = os.environ.get('STRIPE_WH_SECRET')

#  see CI Deployment videos for the below

if 'USE_AWS' in os.environ:
    
    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = 'milestone-four-andrew'
    AWS_S3_REGION_NAME = 'eu-west-2'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
