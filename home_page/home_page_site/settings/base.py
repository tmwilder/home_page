import os.path as op
BASE_DIR = op.dirname(op.dirname(op.dirname(op.abspath(__file__))))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ("tim", "tim@localhost"),
)

ALLOWED_HOSTS = '*'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase',
    }
}

MANAGERS = ADMINS

TIME_ZONE = 'America/Chicago'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = ''

MEDIA_URL = ''

STATIC_ROOT = ''

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    op.join(BASE_DIR, "home_page_site", "static"),
    op.join(BASE_DIR, "home_page_site", "static", "one_files", "HTML")
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = 'x)hd6i)z&s0s81pgimo)mbb8y2vsgywjt23ey@2yrobwq@(qe&'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'home_page_site.urls'

WSGI_APPLICATION = 'home_page_site.wsgi.application'

TEMPLATE_DIRS = (
    op.join(BASE_DIR, "home_page_app", "templates")
)

INSTALLED_APPS = (
    'home_page_app'
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },

    'handlers': {
        'console':{
            'level': 'INFO',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'