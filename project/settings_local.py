DEBUG = True

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql_psycopg2',
       'NAME': 'db4',
       'USER': 'jarek',
       'PASSWORD': 'password',
       'HOST': 'localhost',
       'PORT': '5432',
   },
}
