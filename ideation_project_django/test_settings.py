from ideation_project_django.settings import *


# Database
DATABASES = {
    'default': {
        'ENGINE': environ.get('DB_ENGINE'),
        'NAME': environ.get('TEST_DB_NAME'),
        'USER': environ.get('DB_USER'),
        'PASSWORD': environ.get('DB_PASSWORD'),
        'HOST': environ.get('DB_HOST'),
        'PORT': environ.get('DB_PORT'),
    }
}

USE_TZ = False
