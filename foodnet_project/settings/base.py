"""
Django settings for foodnet project.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

from django.contrib.messages import constants as messages_constants

MESSAGE_TAGS = {
    messages_constants.ERROR: 'danger',
}


BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

ALLOWED_HOSTS = []


AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',

    # invited users only
    'foodnet.membership.auth_backends.InvitationBackend',
)


# Application definition

INSTALLED_APPS = (
    'django_admin_bootstrapped',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # 3rd-party apps.
    'bootstrap3',

    'allauth',
    'allauth.account',
    'captcha',  # django-recaptcha

    # Project apps.
    'foodnet.core',
    'foodnet.membership',
    'foodnet.dashboard',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'foodnet.membership.middleware.NewUserForceProfileMiddleware',
)

ROOT_URLCONF = 'foodnet_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'allauth.account.context_processors.account',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
        },
    },
]


WSGI_APPLICATION = 'foodnet_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

# please use `collectstatic` command
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(asctime)s  [%(name)s:%(lineno)s]  %(levelname)s - %(message)s',
        },
        'simple': {
            'format': '%(levelname)s %(message)s',
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
        }
    },
    'loggers': {
        # Silence SuspiciousOperation.DisallowedHost exception ('Invalid
        # HTTP_HOST' header messages). Set the handler to 'null' so we don't
        # get those annoying emails.
        'django.security.DisallowedHost': {
            'handlers': ['null'],
            'propagate': False,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.db': {
            'handlers': ['console', ],
            'level': 'INFO',
        },
        'foodnet': {
            'handlers': ['console', ],
            'level': 'INFO',
        }
    }
}

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_CONFIRM_EMAIL_ON_GET = False
USER_MODEL_USERNAME_FIELD = 'email'
#ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = LOGIN_URL
#ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_SIGNUP_PASSWORD_VERIFICATION = True
ACCOUNT_USER_DISPLAY = lambda u: u.email
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_PASSWORD_MIN_LENGTH = 8
ACCOUNT_ADAPTER = 'foodnet_project.authnadapter.FoodnetAccountAdapter'
#ACCOUNT_SIGNUP_FORM_CLASS
ACCOUNT_SESSION_REMEMBER = None

SITE_OPEN_FOR_SIGNUP = True

LOGOUT_URL = 'account_logout'
LOGIN_URL = 'account_login'
LOGIN_REDIRECT_URL = 'dashboard:home'

USE_RECAPTCHA = False
RECAPTCHA_PUBLIC_KEY = os.getenv('RECAPTCHA_PUBLIC_KEY', '6LfCEAcTAAAAAJsJhexp8LznEvngOghaw2ckFfq1')
RECAPTCHA_PRIVATE_KEY = os.getenv('RECAPTCHA_PRIVATE_KEY', '')
NOCAPTCHA = False
RECAPTCHA_USE_SSL = False

DATABASES = {}
