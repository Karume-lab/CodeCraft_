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
        "ENGINE": "django.db.backends.mysql",
        "NAME": config("DB_NAME", default="mysql_db", cast=str),
        "USER": config("DB_USER", default="mysql_user", cast=str),
        "PASSWORD": config("DB_PASS", default="mysql_pass", cast=str),
        "HOST": config("DB_HOST", default="localhost", cast=str),
        "PORT": config("DB_PORT", default="3306", cast=str),
    }
}

if config("USE_MYSQL", default=False, cast=bool):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": BASE_DIR / "db.mysql",
        }
    }

# EMAIL SETTINGS
# ==============================================================================

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
