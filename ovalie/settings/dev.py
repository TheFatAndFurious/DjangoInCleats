from .settings import *

# Settings file used for dev

DEBUG=True

STATIC_URL = '/static/'

print(f"{BASE_DIR}")

INTERNAL_IPS = (
    '172.17.0.1',
    '172.18.0.1'
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
         'DIRS': [BASE_DIR / 'news/templates/news'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

STATICFILES_DIRS = [
    BASE_DIR / "static",  # Global static directory (if used)
    BASE_DIR / "news/static/news",
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'news/media')
