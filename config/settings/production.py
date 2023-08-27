from .base import *

# flake8: noqa: F403, F405

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

# ==============================================================================
# EMAIL SETTINGS
# ==============================================================================

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = config("EMAIL_HOST_USER", default=" ")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD", default=" ")
DEFAULT_FROM_EMAIL = config("DEFAULT_FROM_EMAIL", default="test@mail.com")

# ==============================================================================
# SECURITY SETTINGS
# ==============================================================================

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = True

# ==============================================================================
# THIRD-PARTY APPS SETTINGS
# ==============================================================================
