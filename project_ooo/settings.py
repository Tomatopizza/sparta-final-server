"""
Django settings for project_ooo project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
from datetime import timedelta


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

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
    # project app
    'users',
    'articles',
    # django-allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # django-cors-headers
    "corsheaders",
    # django rest framework
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework.authtoken',
    # dj_rest_auth
    'dj_rest_auth',
    'dj_rest_auth.registration',
]


MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project_ooo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # os.path.join(BASE_DIR, 'templates'),
        ],
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

WSGI_APPLICATION = 'project_ooo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_ROOT = BASE_DIR /  "static" 
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
# MEDIA_ROOT = BASE_DIR / "media"
MEDIA_URL = "/media/"
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.User'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ( # 기본적인 view 접근 권한 지정
        'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': ( # session 혹은 token 인증하는 클래스 지정
        # 'rest_framework.authentication.TokenAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PARSER_CLASSES': ( # request.data 속성에 엑세스 할 때 사용되는 파서 지정
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser'
    )
}

# 참고 https://pypi.org/project/django-cors-headers/
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5500",
    "http://127.0.0.1:5500",
]
# CORS_ALLOW_ALL_ORIGINS = True
# CORS_ALLOW_HEADERS = (
#     'authorization',
#     'content-type',
# )


# SIMPLE_JWT = {
#     'ACCESS_TOKEN_LIFETIME': timedelta(minutes=600),
#     'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
#     'SIGNING_KEY': os.environ.get("SECRET_KEY"),
#     'SLIDING_TOKEN_LIFETIME': timedelta(minutes=30),
#     'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
#     "TOKEN_OBTAIN_SERIALIZER": 'users.serializers.CustomTokenObtainPairSerializer',
# }

# 인증 전역 설정(인증 설정 따로 분리하는게 좋긴함)

# REST_AUTH = {
#     'USE_JWT': True,
#     'SESSION_LOGIN': False,
#     'JWT_TOKEN_CLAIMS_SERIALIZER': 'users.serializers.CustomTokenObtainPairSerializer', # 토큰 페이로드 재정의
#     'JWT_AUTH_HTTPONLY':False # refresh 토큰 생성
# }
# REST_USE_JWT = True
# SITE_ID = 1

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com' # 메일 호스트 서버
# EMAIL_PORT = '587' # gmail과 통신하는 포트
# EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER") # 발신할 이메일
# EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD") # 발신할 메일의 비밀번호
# EMAIL_USE_TLS = True # TLS 보안 방법
# DEFAULT_FROM_EMAIL = EMAIL_HOST_USER # 사이트와 관련한 자동응답을 받을 이메일 주소
# URL_FRONT = 'http://****' # 공개적인 웹페이지가 있다면 등록

# ACCOUNT_CONFIRM_EMAIL_ON_GET = True # 유저가 받은 링크를 클릭하면 회원가입 완료되게끔

# EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = '/' # 사이트와 관련한 자동응답을 받을 이메일 주소,'webmaster@localhost'
# ACCOUNT_EMAIL_REQUIRED = False ####### email없이 로그인 가능하게 True -> False 변경
# ACCOUNT_EMAIL_VERIFICATION = "none" ####### 우선 email없이 로그인 가능하게 mandatory -> none 변경 
# ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1
# ACCOUNT_EMAIL_SUBJECT_PREFIX = '[오운완]' #이메일 제목앞에 붙일내용

# AUTHENTICATION_BACKENDS = [
#     # Needed to login by username in Django admin, regardless of `allauth`
#     'django.contrib.auth.backends.ModelBackend',

#     # `allauth` specific authentication methods, such as login by e-mail
#     'allauth.account.auth_backends.AuthenticationBackend',
# ]
WEATHER_KEY = os.environ.get("WEATHER_KEY")


ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = 'http://127.0.0.1:8000/users/allauth/login/' #로그인한 사용자가 없는 경우 이메일 확인 성공 후 지정된 URL로 리디렉션