"""
Django settings for DjangoPro0 project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8-39%=e*q+pz5u@8-9)fy#v1dx82#5p2w*bu(2(^1r#(zgd$y#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []



#this is fro dbname.objects.filter().op()'s failure
LOGGING_CONFIG = 'django.utils.log.dictConfig'

LOGGING = {
    'version':1,
    'disable_existing_loggers':False,
    'handlers':{
        'mail_admins':{
            'level':'ERROR',
            'class':'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers':{
        'django.request':{
            'handlers':['mail_admins'],
            'level':'ERROR',
            'propagate':True,
        }
    }
}

CACHES = {
    'default':{
        'BACKEND':'django.core.cache.backends.locmem.LocMemCache',
    }
}
AUTH_USER_MODEL = 'auth.User'
FORMAT_MODULE_PATH = None
LOCALE_PATHS=()
###########################################

#need these(four) if operate mysql by python
DATABASE_ROUTERS = []
TRANSACTIONS_MANAGED = False
#Mar-16-2016:The tablespaces to use for each model when not specified otherwise
DEFAULT_TABLESPACE = ''
DEFAULT_INDEX_TABLESPACE = ''



# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'DjangoAPP0'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'DjangoPro0.urls'

WSGI_APPLICATION = 'DjangoPro0.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'jango',
        'USER':'root',
        'PASSWORD':'111111',
        'HOST':'',
        'PORT':'',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
