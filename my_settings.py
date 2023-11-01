#my_settings.py
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql', #1
#         'NAME': 'test', #2
#         'USER': 'root', #3
#         'PASSWORD': 'password',  #4
#         'HOST': 'localhost',   #5
#         'PORT': '3306', #6
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pybo',
        'USER': 'dev',
        'PASSWORD': 'hyper2023!dev',
        'HOST': '130.162.154.239',
        'PORT': '5432',
    }
}



SECRET_KEY ='f$lm%lvrt!@62h+$p=_cxqu21h$*auv-!aj)%4e&jb5lkg5c(+'

