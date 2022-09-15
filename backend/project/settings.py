"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 3.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from datetime import timedelta

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from django.core.exceptions import ImproperlyConfigured

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', '!94cvjzfvjm9u%q&6dfsgx0_t$^vd_7(%v(h008)kiayb8b2%*')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = int(os.environ.get("DEBUG", default=0)) == 0

ALLOWED_HOSTS = ['localhost', 'apps.avantrio.xyz', os.environ.get('APP_HOST', '')]

# Application definition

INSTALLED_APPS = [
    'safedelete',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'apps.common',
    'apps.files',
    'apps.users',
    'apps.appoinments',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'emails')],
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

WSGI_APPLICATION = 'project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DATABASE_NAME', 'boilerplate'),
        'USER': os.environ.get('DATABASE_USER', 'root'),
        'PASSWORD': os.environ.get('DATABASE_PWD', 'admin'),
        'HOST': os.environ.get('DATABASE_HOST', 'localhost'),
        'PORT': os.environ.get("DATABASE_PORT", '5432'),
        'TEST': {
            'NAME': 'boilerplate_test',
        },
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = os.getenv('DJANGO_TIME_ZONE', 'UTC')

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = os.getenv('DJANGO_STATIC_URL', '/static/')

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    'DEFAULT_RENDERER_CLASSES': (
        'project.renderer.CustomJSONRenderer',
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'EXCEPTION_HANDLER': 'project.exception_handler.custom_exception_handler',
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    )
}

# file upload parameters
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=os.environ.get('SIMPLE_JWT_ACCESS_TOKEN_LIFETIME', 5)),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=os.environ.get('SIMPLE_JWT_REFRESH_TOKEN_LIFETIME', 30))
}

AUTH_USER_MODEL = 'users.User'

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

EMAIL_HOST = os.getenv('DJANGO_EMAIL_HOST', 'smtp.sendgrid.net')
EMAIL_HOST_USER = os.getenv('DJANGO_EMAIL_HOST_USER', 'apikey')
EMAIL_HOST_PASSWORD = os.getenv('DJANGO_EMAIL_HOST_PASSWORD', 'SG.NSMxsd4pSWeAzRsdDXk5OA'
                                                              '.CsLPvWjekYtc2AQH5oJYtXg81g20kWnCKSwy9a5lb7o')
EMAIL_PORT = os.getenv('DJANGO_EMAIL_PORT', 587)
EMAIL_USE_TLS = os.getenv('DJANGO_EMAIL_USE_TLS', True)
EMAIL_FROM_ADDRESS = os.getenv('DJANGO_EMAIL_FROM_ADDRESS', 'support@project.apps.avantrio.xyz')

# Send Emails to console when DEBUG is on
if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

APP_URL = os.environ.get('APP_HOST', 'http://localhost')

# TWILIO SMS Config
TWILIO_SID = os.getenv('TWILIO_SID', "")
TWILIO_TOKEN = os.getenv('TWILIO_TOKEN', "")

# Custom Config
VERIFY_EMAIL = os.getenv('DJANGO_VERIFY_EMAIL', True)
INVITE_USERS = os.getenv('DJANGO_VERIFY_EMAIL', False)
SELF_REGISTER = os.getenv('DJANGO_SELF_REGISTER', True)

# File Upload Config
ANONYMOUS_FILE_UPLOAD = os.getenv('DJANGO_ANONYMOUS_FILE_UPLOAD', True)

# Storage Configuration
# Default Storage Types: AWS, DEFAULT for local storage
DEFAULT_STORAGE = os.getenv('DJANGO_DEFAULT_STORAGE', 'DEFAULT')
OVERRIDE_DEFAULT_STORAGE_IN_DEBUG = os.getenv('DJANGO_OVERRIDE_DEFAULT_STORAGE_IN_DEBUG', True)

if DEBUG and not OVERRIDE_DEFAULT_STORAGE_IN_DEBUG and not DEFAULT_STORAGE == 'DEFAULT':
    raise ImproperlyConfigured(
        f'''
        Provided storage type '{DEFAULT_STORAGE}' cannot be used in DEBUG mode without proper configuration.
        Please set 'DJANGO_OVERRIDE_DEFAULT_STORAGE_IN_DEBUG' to True if you need to test external storage.
        '''
    )

# AWS Config
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID', '')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY', '')
AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME', '')
AWS_S3_OBJECT_PARAMETERS = os.getenv('AWS_S3_OBJECT_PARAMETERS', {})
AWS_S3_FILE_OVERWRITE = os.getenv('AWS_S3_FILE_OVERWRITE', False)
AWS_LOCATION = os.getenv('AWS_LOCATION', '')
AWS_S3_REGION_NAME = os.getenv('AWS_S3_REGION_NAME', None)
AWS_S3_USE_SSL = os.getenv('AWS_S3_USE_SSL', True)
AWS_S3_ENDPOINT_URL = os.getenv('AWS_S3_ENDPOINT_URL', None)
AWS_S3_VERIFY = os.getenv('AWS_S3_VERIFY', None)

if DEFAULT_STORAGE == 'AWS':
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'

    if not all([AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME]):
        raise ImproperlyConfigured(
            f'''
            One or more config items are not present.
            Please check the configuration again.
            Required Configs:
                - AWS_ACCESS_KEY_ID {'[✓]' if AWS_ACCESS_KEY_ID != '' else '[X]'}
                - AWS_SECRET_ACCESS_KEY {'[✓]' if AWS_SECRET_ACCESS_KEY != '' else '[X]'}
                - AWS_STORAGE_BUCKET_NAME {'[✓]' if AWS_STORAGE_BUCKET_NAME != '' else '[X]'}
            '''
        )

# Broker Configuration
BROKER_USER = os.environ.get("BROKER_USER", "broker_admin")
BROKER_PASSWORD = os.environ.get("BROKER_PASSWORD", "admin@11235")
BROKER_HOST = os.environ.get("BROKER_HOST", "localhost")
BROKER_PORT = os.environ.get("BROKER_PORT", 5672)

# Async Config
ENABLE_CELERY = os.getenv('ENABLE_CELERY', False)

# celery Configuration
if ENABLE_CELERY:
    CELERY_TASK_TRACK_STARTED = True
    CELERY_BROKER_URL = f"amqp://{BROKER_USER}:{BROKER_PASSWORD}@{BROKER_HOST}:{BROKER_PORT}"
    CELERY_BACKEND_URL = os.environ.get("CELERY_BACKEND_URL", 'redis://localhost:6379/0')
    CELERY_TASK_ACKS_LATE = True
    CELERY_WORKER_PREFETCH_MULTIPLIER = 1

# Zappa Config
ENABLE_ZAPPA = os.getenv('ENABLE_ZAPPA', False)
ZAPPA_AWS_REGION = os.getenv('ZAPPA_AWS_REGION', '')

# Test runner
TEST_RUNNER = 'project.pytest_runner.PytestTestRunner'
