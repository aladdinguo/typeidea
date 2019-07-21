from .base import *  # NOQA

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
