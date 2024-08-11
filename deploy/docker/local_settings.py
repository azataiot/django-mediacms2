import os

FRONTEND_HOST = os.getenv('FRONTEND_HOST', 'http://localhost')
PORTAL_NAME = os.getenv('PORTAL_NAME', 'MediaCMS')
SECRET_KEY = os.getenv('SECRET_KEY', 'ma!s3^b-cw!f#7s6s0m3*jx77a@riw(7701**(r=ww%w!2+yk2')
POSTGRES_HOST = os.getenv('POSTGRES_HOST', 'db')
POSTGRES_PORT = os.getenv('POSTGRES_PORT', '5432')
REDIS_LOCATION = os.getenv('REDIS_LOCATION', "redis://192.168.1.139:32761/1")
POSTGRES_DB = os.getenv('POSTGRES_DB', 'mediacms')
POSTGRES_USER = os.getenv('POSTGRES_USER', 'mediacms')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'mediacms')

TIME_ZONE = "Europe/Istanbul"
PORTAL_WORKFLOW = "public"
REGISTER_ALLOWED = False

# email settings
DEFAULT_FROM_EMAIL = "info@azat.host"
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', 'password')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', 'info@azat.host')
SERVER_EMAIL = DEFAULT_FROM_EMAIL
EMAIL_HOST = os.getenv('EMAIL_HOST', 'mail.azat.host')
EMAIL_PORT = os.getenv('EMAIL_PORT', 587)
ADMIN_EMAIL_LIST = ["info@azat.host"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": POSTGRES_DB,
        "HOST": POSTGRES_HOST,
        "PORT": POSTGRES_PORT,
        "USER": POSTGRES_USER,
        "PASSWORD": POSTGRES_PASSWORD,
    }
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_LOCATION,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}

# CELERY STUFF
BROKER_URL = REDIS_LOCATION
CELERY_RESULT_BACKEND = BROKER_URL

MP4HLS_COMMAND = "/home/mediacms.io/bento4/bin/mp4hls"

DEBUG = os.getenv('DEBUG', True)
