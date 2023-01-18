"""
Django settings for Alteernlingual project.

Generated by 'django-admin startproject' using Django 3.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-uaw9$t28qnof!kj+#lju9r-c43z^gj8qxax!n#=(v-0)*5j6_n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['192.168.43.225', '127.0.0.1', '*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sitemaps' ,
    'django.contrib.sites',
    'alteernlingual_user',
    'Alteernlingual_topic',    
    'crispy_forms',
    'ckeditor',
    'allauth', 
    'allauth.account', 
    'allauth.socialaccount',     
    'allauth.socialaccount.providers.facebook',    

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Alteernlingual.urls'

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





SOCIAL_AUTH_FACEBOOK_KEY = '454152439240824'  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = 'b7e00649c097ea5b8000ef2105d6b5a7'  # App Secret


LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'home'


WSGI_APPLICATION = 'Alteernlingual.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'alteernlingual_db2',
        'USER': 'postgres',
        'PASSWORD': '1234Asdf##',
        'HOST': 'localhost',
        'PORT': '',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

from django.utils.translation import gettext_noop

LANGUAGES = [

    ('ar', gettext_noop('Arabic')),
    ('en', gettext_noop('English')),
    ('fr', gettext_noop('French')),
    ('ha', gettext_noop('hausa')),
    ('ig', gettext_noop('Igbo')),
    ('yo', gettext_noop('Yoruba')),    
]

EXTRA_LANG_INFO = {
    
    'ig': {
        'bidi': False,  # right-to-left
        'code': 'ig',
        'name': 'Igbo',
        'name_local': "Igbo",
    },

    'ha': {
        'bidi': False,  # right-to-left
        'code': 'ha',
        'name': 'Hausa',
        'name_local': "Hausa",
    },

    'yo': {
        'bidi': False,  # right-to-left
        'code': 'yo',
        'name': 'Yoruba',
        'name_local': "Yoruba",
    },
    
}


# Add custom languages not provided by Django
import django.conf.locale
LANG_INFO = dict(django.conf.locale.LANG_INFO, **EXTRA_LANG_INFO)
django.conf.locale.LANG_INFO = LANG_INFO

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]


TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'




STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'alteernlingual_user/static'),
]

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGOUT_REDIRECT_URL = 'login'
LOGIN_REDIRECT_URL = 'dashboard'


DEFAULT_FROM_EMAIL = 'a.damilare2012@gmail.com'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
MAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'a.damilare2012@gmail.com'
EMAIL_HOST_PASSWORD = 'wazobiawazobia'
EMAIL_PORT = 587


EMAIL_FILE_PATH = str(BASE_DIR.joinpath('sent_emails'))

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'alteernlingual_user/media')

# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Third party apps configuration

CRISPY_TEMPLATE_PACK = 'bootstrap4'


CKEDITOR_UPLOAD_PATH = "CK_uploads/"

CKEDITOR_CONFIGS = {


    'default': {'toolbar': 'full','extraPlugins': ','.join(['html5audio',]),},

            }

SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'APP': {
            'client_id': '454152439240824',
            'secret': 'b7e00649c097ea5b8000ef2105d6b5a7',
            'key': '',
            'scope': ['email'],
        }
    }
}            


SITE_ID = 1


ACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_AUTHENTICATION_METHOD = "facebook"
ACCOUNT_EMAIL_REQUIRED = False

LOGIN_REDIRECT_URL = "/" 