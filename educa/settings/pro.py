from .base import *
DEBUG = False
ADMINS = (
    ('admin', 'admin@gmail.com'),
)
ALLOWED_HOSTS = ['educaproject.com', 'www.educaproject.com']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'educa',
        'USER': 'educa',
        'PASSWORD': 'educa',
    }
}