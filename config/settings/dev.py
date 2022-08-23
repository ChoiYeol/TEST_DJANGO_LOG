from .base import *
from dotenv import load_dotenv
load_dotenv(verbose=True) #.env가 누락일경우 경고메시지 출력하는옵션
 
 
 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': os.environ.get("DB_NAME_DEV"),
        'USER': os.environ.get("WRITE_DB_USER_DEV"),
        'PASSWORD': os.environ.get("WRITE_DB_PASSWORD_DEV"),
        'HOST': os.environ.get("WRITE_DB_HOST_DEV"),
        'PORT': os.environ.get("WRITE_DB_PORT_DEV"),
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        },
    },
    'replica': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get("DB_NAME_DEV"),
        'USER': os.environ.get("READ_DB_USER_DEV"),
        'PASSWORD': os.environ.get("READ_DB_PASSWORD_DEV"),
        'HOST': os.environ.get("READ_DB_HOST_DEV"),
        'PORT': os.environ.get("READ_DB_PORT_DEV"),
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        },
    },
}
 
   