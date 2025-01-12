"""
Django settings for myproject project.

Generated by 'django-admin startproject' using Django 5.1.3.

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
# SECRET_KEY = 'django-insecure-d9v2l^qn+bw=ahttki7h(tqpmilm#p578+2v7c1llp+)2rqs+)'
SECRET_KEY = os.getenv('SECRET_KEY') #продакшен

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False #когда продакшен меняем на фолс
SESSION_COOKIE_SECURE = True #продакшен
CSRF_COOKIE_SECURE = True #продакшен

ALLOWED_HOSTS = [
    # '127.0.0.1', #локальный адрес
    # '95.24.11.44', #айпи ноута вводим на телефоне и видно сервер
    'Belloocha11.pythonanywhere.com', #продакшен

]

INTERNAL_IPS = [
    '127.0.0.1', #дописали для отладки эту константу
]
# Application definition

INSTALLED_APPS = [ 
    'django.contrib.admin', #админка
    'django.contrib.auth', #авторизации
    'django.contrib.contenttypes', #контент
    'django.contrib.sessions', #сессии запоминаем пользователя при некст заходе 
    'django.contrib.messages', #отправка сообщения
    'django.contrib.staticfiles', # статические файлы
    'myapp',
    'myapp2',
    'myapp3',
    'myapp4',
    'myapp5',
    'myapp6',
    'debug_toolbar',
]

MIDDLEWARE = [ #промежуточное по
    'debug_toolbar.middleware.DebugToolbarMiddleware', #добавили
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
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

WSGI_APPLICATION = 'myproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
DATABASES = { #продакшен
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Belloocha11$default',
        'USER': 'Belloocha11',
        'PASSWORD': os.getenv('MYSQL_PASSWORD'),
        'HOST': 'Belloocha11.mysql.pythonanywhere-services.com',
        'OPTIONS': {
            'init_command': "SET NAMES 'utf8mb4';SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4', #любой язык
        },
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'ru-ru' #'en-us' язык

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static/' #продакшен

MEDIA_URL = '/media/' #адрес медиа
MEDIA_ROOT = BASE_DIR / 'media' #каталог

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGGING = { 
    'version': 1, #стандартная запись
    'disable_existing_loggers': False, #не отключаем существующие логи т.к. фолс
    'formatters': { 
        'verbose': { #подробное форматирование
            'format': '{levelname} {asctime} {module} {process} {thread} {message}', # asctime - время когда произошло событие модуль процесс и поток
            'style': '{', #стиль форматирования фигурные скобки
        }, 
        'simple': { #обычное форматирование
            'format': '%(levelname)s %(message)s' #уровень логгера
        }, 
    }, 
    'handlers': { #обработчики
        'console': { #в консоль
            'class': 'logging.StreamHandler', 
            'formatter': 'verbose',  # форматирование для  обработчика консольного 
        }, 
        'file': { #в файл
            'class': 'logging.FileHandler', 
            'filename': './log/django.log', #путь к файлу c логами
            'formatter': 'verbose',  # форматирование для  обработчика в файл 
        }, 
    }, 
    'loggers': { 
        'django': { #1 логер хочу логировать все данные приложения джанго
            'handlers': ['console', 'file'], 
            'level': 'INFO', 
        }, 
        'myapp': { #для приложения меняем в зависимости от приложеняи с которым работаем
            'handlers': ['console', 'file'],
            'level': 'DEBUG', 
            'propagate': True, #если есть высоко стоящие логеры я хочу их использовать
        },
        'myapp4': { #для приложения меняем в зависимости от приложеняи с которым работаем
            'handlers': ['console', 'file'],
            'level': 'DEBUG', 
            'propagate': True, #если есть высоко стоящие логеры я хочу их использовать
        },
    }, 
} 
