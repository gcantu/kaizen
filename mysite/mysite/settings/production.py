from .base import *

config.read('/etc/kaizen/settings.ini')


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config.get('keys','SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['18.222.117.200', 'ec2-18-222-117-200.us-east-2.compute.amazonaws.com']

# Database
DATABASES = {
'default': {
    'ENGINE': 'django.db.backends.mysql',
    'OPTIONS': {
        'read_default_file': '/etc/mysql/my.cnf',
    },
}
}


STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
