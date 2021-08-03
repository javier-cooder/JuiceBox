import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

from django.core.wsgi import get_wsgi_application

DATABASE = {
    'default' :{
        'ENGINE': 'django.db.backends.sqlite3'
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
