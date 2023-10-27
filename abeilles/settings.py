import os
from pathlib import Path

ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent.parent

BASE_DIR = Path(__file__).resolve().parent.parent

PROJECT_ROOT = Path(__file__).resolve().parent

TEMPLATE_DIR = str(BASE_DIR / 'templates')

STATICFILES_DIRS = [
        str(PROJECT_ROOT / 'static'),
    ]

MEDIA_ROOT = str(BASE_DIR / 'media/')

MEDIA_URL = '/media/'

STATIC_PATH = '/staticfiles'

EMAIL_USE_TLS = False


from .settings_specific import *

STATIC_ROOT = str(ROOT_DIR / STATIC_PATH)

INSTALLED_APPS = [
    'ckeditor',
    'ckeditor_uploader',
    'honeypot',
    'users.apps.UsersConfig',
    'services.apps.ServicesConfig',
    'basket.apps.BasketConfig',
    'posts.apps.PostsConfig',
    'pages.apps.PagesConfig',
    'questions.apps.QuestionsConfig',
    'settings.apps.SettingsConfig',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'abeilles.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'pages.context_processors.webforms',
                'pages.context_processors.menu_categories',
                'pages.context_processors.benefits',
                'pages.context_processors.garden_benefits',
                'pages.context_processors.social_links',
            ],
        },
    },
]

WSGI_APPLICATION = 'abeilles.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

AUTHENTICATION_BACKENDS = (
    'users.accounts.backends.EmailOrUsernameModelBackend',
    'django.contrib.auth.backends.ModelBackend',
)

LANGUAGE_CODE = 'fr-FR'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


#ckeditor settings
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_IMAGE_BACKEND = 'pillow'
# CKEDITOR_UPLOAD_PATH = os.path.join(MEDIA_ROOT, "uploads")
CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_CONFIGS = {
   'default': {
       'toolbar_Full': [
            ['Bold', 'Italic', 'Underline', 'Strike',],
            ['NumberedList','BulletedList'],
            ['Link', 'Unlink', 'Anchor'],
            ['Blockquote', 'Table'],
            ['Format',],
            ['RemoveFormat',],
            ['Source'],
            ['Image',],
        ],
        'extraPlugins': 'justify,liststyle,indent',
   },
}

CKEDITOR_BROWSE_SHOW_DIRS = True
