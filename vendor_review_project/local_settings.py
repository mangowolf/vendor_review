import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'vendor_review',
        'USER': 'jimmy',
        'PASSWORD': 'Bonner8187642396!',
        'HOST': 'localhost',
        'PORT': '',
    }
}

DEBUG = True