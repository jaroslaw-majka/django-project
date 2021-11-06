DEBUG = True

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql_psycopg2',
       'NAME': 'da3',
       'USER': 'jarek',
       'PASSWORD': 'password',
       'HOST': 'localhost',
       'PORT': '5432',
   },
}
