# Add 'myapp' and 'rest_framework' to INSTALLED_APPS

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',
    'rest_framework',
]

# Change database to MySQL

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'parking',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': '',
        'PORT': '',
    }
}

# Change TIME_ZONE

TIME_ZONE = 'America/New_York'
