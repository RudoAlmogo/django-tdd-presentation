from .base import *  # noqa


DEFAULT_FILE_STORAGE = 'tdd.storage.InMemoryStorage'

# Use MD5PasswordHasher for faster tests
PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]
