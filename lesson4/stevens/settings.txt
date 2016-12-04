# Edit settings.py that was generated from the command 'django-admin startproject stevens'
# Add 'myapp' to INSTALLED_APPS

INSTALLED_APPS = [
                  'django.contrib.admin',
                  'django.contrib.auth',
                  'django.contrib.contenttypes',
                  'django.contrib.sessions',
                  'django.contrib.messages',
                  'django.contrib.staticfiles',
                  'myapp', # add this line
]

# Change database to MySQL

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # change sqlite3 to mysql
        'NAME': 'stevens', # change os.path.join(BASE_DIR, 'db.sqlite3') to stevens
	'USER': 'root', # mysql root user
        'PASSWORD': 'password', # mysql root password
        'HOST': '', # set to empty for localhost
        'PORT': '', # set to empty for default port
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

# Change TIME_ZONE

TIME_ZONE = 'America/New_York'
