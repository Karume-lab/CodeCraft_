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
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("DB_NAME", default="postgres_db", cast=str),
        "USER": config("DB_USER", default="postgres_user", cast=str),
        "PASSWORD": config("DB_PASS", default="postgres_pass", cast=str),
        "HOST": config("DB_HOST", default="localhost", cast=str),
        "PORT": config("DB_PORT", default="5432", cast=str),
    }
}

if config("USE_SQLITE", default=False, cast=bool):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
