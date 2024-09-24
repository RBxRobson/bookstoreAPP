"""
Django settings for bookstore project.

Generated by 'django-admin startproject' using Django 5.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-drs=t$s77ekre$k0f$6-&i-1sr898fpeyhum1hx(#b20cqhkqx"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_extensions",
    "order", 
    "product",
    "rest_framework",
    "rest_framework.authtoken",
    "debug_toolbar"
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = "bookstore.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "bookstore.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# Configurações de banco de dados
DATABASES = {
    "default": {
        # Define o engine do banco de dados (por padrão, SQLite)
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
        # Define o nome do banco de dados ou o caminho do arquivo SQLite
        "NAME": os.environ.get("SQL_DATABASE", BASE_DIR / "db.sqlite3"),
        # Usuário do banco de dados (padrão: 'user')
        "USER": os.environ.get("SQL_USER", "user"),
        # Senha do banco de dados (padrão: 'password')
        "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
        # Host do banco de dados (padrão: 'localhost')
        "HOST": os.environ.get("SQL_HOST", "localhost"),
        # Porta do banco de dados (padrão: 5432 para PostgreSQL)
        "PORT": os.environ.get("SQL_PORT", "5432"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 5,
    # Define as classes de autenticação padrão a serem usadas.
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # BasicAuthentication usa nome de usuário e senha enviados no cabeçalho HTTP.
        'rest_framework.authentication.BasicAuthentication',
        # SessionAuthentication usa a sessão do Django para autenticar usuários (usando cookies).
        'rest_framework.authentication.SessionAuthentication',
        # TokenAuthentication usa tokens para autenticar os usuários.
        # Cada usuário recebe um token único que deve 
        # ser enviado no cabeçalho HTTP Authorization
        # como 'Token <seu_token>' para autenticação em cada requisição.
        'rest_framework.authentication.TokenAuthentication'

    ]
}

# Define os IPs internos para uso durante o desenvolvimento (ex.: com o Django Debug Toolbar)
INTERNAL_IPS = [
    "127.0.0.1",
]

# Obtém a chave secreta do Django a partir das variáveis de ambiente
SECRET_KEY = os.environ.get("SECRET_KEY")

# Define se o modo de depuração está ativado (0: desativado, 1: ativado)
DEBUG = int(os.environ.get("DEBUG", default=0))

# 'DJANGO_ALLOWED_HOSTS' deve ser uma string de hosts separados por espaços.
# Exemplo de variável de ambiente: 'DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]'
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")
