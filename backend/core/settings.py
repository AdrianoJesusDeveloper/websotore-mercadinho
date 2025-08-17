# mercadinho_backend/settings.py
import os
from pathlib import Path
from datetime import timedelta
from dotenv import load_dotenv

# carrega variáveis do .env na raiz do projeto
load_dotenv()  # lê .env e injeta no os.environ

# BASE_DIR = pasta do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY segura a sessão/assinaturas do Django
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "dev-secret")

# DEBUG True em dev; em produção usar False
DEBUG = os.getenv("DJANGO_DEBUG", "False") == "True"

# hosts permitidos (em produção adicionar domínio)
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "localhost,127.0.0.1").split(",")

# apps instaladas (Django + terceiros + nossas apps)
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",            # auth padrão (vamos customizar model)
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # 3rd party
    "rest_framework",                 # DRF
    "corsheaders",                    # CORS
    "drf_spectacular",                # OpenAPI/Swagger
    # apps do projeto
    "accounts",
    "catalog",
    "cart",
    "orders",
    "payments",
    "products",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",            # deve vir acima do CommonMiddleware
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],  # caso tenha templates
        "APP_DIRS": True,
        "OPTIONS": {"context_processors": ["django.template.context_processors.debug",
                                           "django.template.context_processors.request",
                                           "django.contrib.auth.context_processors.auth",
                                           "django.contrib.messages.context_processors.messages"]},
    }
]

WSGI_APPLICATION = "core.wsgi.application"

# DATABASE: configura MySQL via env
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",      # usa mysqlclient
        "NAME": os.getenv("DB_NAME", "mercadinho_db"),
        "USER": os.getenv("DB_USER", "root"),
        "PASSWORD": os.getenv("DB_PASSWORD", ""),
        "HOST": os.getenv("DB_HOST", "localhost"),
        "PORT": os.getenv("DB_PORT", "3306"),
        "OPTIONS": {"init_command": "SET sql_mode='STRICT_TRANS_TABLES'"},
    }
}

# Password validators (boas práticas)
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator", "OPTIONS": {"min_length": 8}},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internacionalização e fuso
LANGUAGE_CODE = "pt-br"
TIME_ZONE = "America/Sao_Paulo"
USE_I18N = True
USE_L10N = True
USE_TZ = True

# arquivos estáticos e mídia
STATIC_URL = "/static/"
MEDIA_URL = os.getenv("MEDIA_URL", "/media/")
MEDIA_ROOT = os.path.join(BASE_DIR, os.getenv("MEDIA_ROOT", "media"))

# Cors: permitir origens do frontend (VITE)
CORS_ALLOWED_ORIGINS = os.getenv("CORS_ALLOWED_ORIGINS", "http://localhost:5173").split(",")

# Autenticação custom user
AUTH_USER_MODEL = "accounts.User"  # aponta para nosso model customizado accounts.User

# REST FRAMEWORK: usar JWT e gerar docs
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticatedOrReadOnly",),
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 12,
}

# Simple JWT configs
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=int(os.getenv("JWT_ACCESS_MINUTES", 15))),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=int(os.getenv("JWT_REFRESH_DAYS", 7))),
    "AUTH_HEADER_TYPES": ("Bearer",),
}

# drf-spectacular (OpenAPI)
SPECTACULAR_SETTINGS = {
    "TITLE": "Mercadinho API",
    "DESCRIPTION": "API REST para WebStore de Mercadinho", 
    "VERSION": "1.0.0",
}
