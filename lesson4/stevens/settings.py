# Add 'myapp' to INSTALLED_APPS

INSTALLED_APPS = [
                  'django.contrib.admin',
                  'django.contrib.auth',
                  'django.contrib.contenttypes',
                  'django.contrib.sessions',
                  'django.contrib.messages',
                  'django.contrib.staticfiles',
                  'myapp',
]

# Change database to MySQL

DATABASES = {
    'defalut': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'stevens',
	'USER': 'root',
        'PASSWORD': 'password',
        'HOST': '', # set to empty for localhost
        'PORT': '', # set to empty for default port
    }
}

# Change TIME_ZONE

TIME_ZONE = 'America/New_York'
