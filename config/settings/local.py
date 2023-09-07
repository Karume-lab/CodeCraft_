# flake8: noqa: F403, F405
from .base import *

INSTALLED_APPS += ["debug_toolbar"]

MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")

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

# EMAIL SETTINGS
# ==============================================================================

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "tech.codecraft1@gmail.com"
EMAIL_HOST_PASSWORD = "zvfqlequcqlryqbm"
DEFAULT_FROM_EMAIL = "contactus@codecraft.tech"
