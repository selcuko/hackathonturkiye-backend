import os
import uuid
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = os.getenv("SECRET_KEY", str(uuid.uuid4()))

DEBUG = True

ALLOWED_HOSTS = [
    'localhost',                        # Gunicorn needs this
    'jacqueline',                       # Local development environment
    'testserver',                       # Used for unit testing
    'ht.omerselcuk.engineer',
    'api.hackathonturkiye.com',
    '209.97.180.252',
]

CORS_ORIGIN_WHITELIST = [
    'https://hackathonturkiye.com',
    'http://hackathonturkiye.com',
    'http://209.97.180.252',
    'http://209.97.180.252:4000',
    'http://127.0.0.1:4000',
    'http://127.0.0.1',
#    'localhost',
#    'http://127.0.0.1',
]
CORS_ORIGIN_ALLOW_ALL = True  # Testing something...

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10,

    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ]
}


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': './debug.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

# Application definition

INSTALLED_APPS = [
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'drf_yasg',
    'djrichtextfield',
    'profile.apps.ProfileConfig',
    'blog.apps.BlogConfig',
    'event.apps.EventConfig',
    'contact.apps.ContactConfig',
    'common',
    'hosting',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hackathonturkiye.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'hackathonturkiye.wsgi.application'

DATABASES = {
    'default': dj_database_url.parse(os.getenv(
        'DATABASE_URL',
        'postgres://amy:amy@localhost:5432/htdb'
        ))
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

TIME_ZONE = 'Europe/Istanbul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


DJRICHTEXTFIELD_CONFIG = {
    'js': [f'//cdn.tiny.cloud/1/{os.getenv("TINYMCE_API", "no-api-key")}/tinymce/5/tinymce.min.js'],
    'init_template': 'djrichtextfield/init/tinymce.js',
    'settings': {
        'relative_urls' : False,
        'remove_script_host' : False,
        'resize': 'both',
        'document_base_url' : 'https://api.hackathonturkiye.com/',
        'block_formats': 'Paragraph=p; Heading 2=h2; Heading 3=h3; Heading 4=h4; Heading 5=h5; Heading 6=h6; Preformatted=pre',
        'menubar': 'file edit insert view format table tools help',
        'plugins': 'autoresize media link image autosave lists autolink code',
        'toolbar': 'undo redo | formatselect | bold italic underline fontselect fontsizeselect | link image media | removeformat',
        #'width': 900,
        'menu': {
            'file': { 'title': 'File', 'items': 'newdocument restoredraft | preview | print ' },
            'edit': { 'title': 'Edit', 'items': 'undo redo | cut copy paste | selectall | searchreplace' },
            'view': { 'title': 'View', 'items': 'code | visualaid visualchars visualblocks | spellchecker | preview fullscreen' },
            'insert': { 'title': 'Insert', 'items': 'image link media template codesample inserttable | charmap emoticons hr | pagebreak nonbreaking anchor toc | insertdatetime' },
            'format': { 'title': 'Format', 'items': 'bold italic underline strikethrough superscript subscript codeformat | formats blockformats fontformats fontsizes align | forecolor backcolor | removeformat' },
            'tools': { 'title': 'Tools', 'items': 'spellchecker spellcheckerlanguage | code wordcount' },
            'table': { 'title': 'Table', 'items': 'inserttable | cell row column | tableprops deletetable' },
            'help': { 'title': 'Help', 'items': 'help' }
        },
        'content_css':[
            '//fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap',
            '//fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap',
            '//fonts.googleapis.com/css2?family=Nunito:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap',
            '//fonts.googleapis.com/css2?family=Fairplay+Display:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap'
        ],
        'font_formats':'Fairplay Display=fairplay display;Roboto=roboto;Nunito=nunito;Montserrat=montserrat;Andale Mono=andale mono,times;Arial=arial,helvetica,sans-serif;Arial Black=arial black,avant garde;Book Antiqua=book antiqua,palatino;Comic Sans MS=comic sans ms,sans-serif;Courier New=courier new,courier;Georgia=georgia,palatino;Helvetica=helvetica;Impact=impact,chicago;Symbol=symbol;Tahoma=tahoma,arial,helvetica,sans-serif;Terminal=terminal,monaco;Times New Roman=times new roman,times;Trebuchet MS=trebuchet ms,geneva;Verdana=verdana,geneva;Webdings=webdings;Wingdings=wingdings,zapf dingbats',
        'fontsize_formats': '8pt 10pt 12pt 14pt 18pt 19pt 20pt 22pt 24pt 36pt 48pt 72pt',
    }
}
