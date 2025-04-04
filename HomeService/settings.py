import environ
env = environ.Env()
environ.Env.read_env()

from datetime import timedelta
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-3q+kki&bn&%m+^tq0x81)^po(7tf+%!!d+m&abbka12)orf$t2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # jwt authentication
    'rest_framework',
    'rest_framework_simplejwt',
    'dj_rest_auth',
    'dj_rest_auth.registration',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    "rest_framework.authtoken",
    'corsheaders',
    # my apps
    'authentications',
    'categories',
    'categoriesPage',
    'services',
    'review',
    'user',
    'blog',
    
    'rest_framework_simplejwt.token_blacklist',

]


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (

        'rest_framework.authentication.TokenAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
}


AUTH_USER_MODEL = 'authentications.CustomUser'

# Stripe Keys
STRIPE_SECRET_KEY = "sk_test_51RA0154Ft3OiftBEd9PpE2Kul7t2qVWHmFzejAXx3XiUyUn3JjjkYjkB7HimML7Bv8u7TYHU5Z2FCB3kmkkGCqfB00S5nF2yAc"
STRIPE_PUBLISHABLE_KEY = "pk_test_51RA0154Ft3OiftBEBdRpJAIRlRHPws30OrFnt6a8DBRDrCHT0dRv4KYXA0oIpFErU1Q3wYhyiae79m4UxUEFTy5R00vD5wDRHa"

# JWT Settings

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=5),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    # Replace with your secret key
    'SIGNING_KEY': 'django-insecure-3q+kki&bn&%m+^tq0x81)^po(7tf+%!!d+m&abbka12)orf$t2',
}

#  email verification
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'foysal.cse11@gmail.com'
EMAIL_HOST_PASSWORD = 'swxnxvdtcshucviv'

REST_USE_JWT = True
SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('Bearer',),
}
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # jwt
    "allauth.account.middleware.AccountMiddleware",
]
CORS_ALLOW_ALL_ORIGINS = True
ROOT_URLCONF = 'HomeService.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'HomeService.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# EMAIL=foysal.cse11@gmail.com
# EMAILPASSWORD=szvisvfphewtlcma
# 2nd
# EMAILPASSWORD=swxn xvdt cshu cviv

# EMAIL=foysal.cse11@gmail.com
# loginPass : Goy%%s33

# token : 92a2cc4cd5170380b47c723009b49509ecfec56b
