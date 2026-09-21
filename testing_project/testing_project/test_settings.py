from django.conf.global_settings import PASSWORD_HASHERS

from testing_project.settings import *

MAINTENANCE_MODE = False

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.MD5PasswordHasher"
]