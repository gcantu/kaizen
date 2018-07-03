
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

from .base import *

config.read('/usr/local/etc/settings.ini')


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config.get('keys','SECRET_KEY')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'OPTIONS': {
            'option_files': '/usr/local/etc/my.cnf',
            'use_pure': True,
        },
    }
}
