# flake8: noqa: F403, F401
from .base import *

PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]


class DisableMigrations:
    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return None


MIGRATION_MODULES = DisableMigrations()

# ==============================================================================
# DATABASES SETTINGS
# ==============================================================================
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
# ==============================================================================


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": config("DB_NAME", default="mysql_db", cast=str),
        "USER": config("DB_USER", default="mysql_user", cast=str),
        "PASSWORD": config("DB_PASS", default="mysql_pass", cast=str),
        "HOST": config("DB_HOST", default="localhost", cast=str),
        "PORT": config("DB_PORT", default="", cast=str),
    }
}

if config("USE_MYSQL", default=False, cast=bool):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": BASE_DIR / "db.mysql",
        }
    }
