"""
Django settings for cmdb_hls project.

Generated by 'django-admin startproject' using Django 4.0.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

from pathlib import Path
import os
import logging

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_BASE_DIR = os.path.join(BASE_DIR, 'config')  # 配置基本路径
SCRIPT_BASE_DIR = os.path.join(BASE_DIR, 'scripts')  # 脚本基本路径

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-pxd7z829uyzyy=q!6+vju=21v290%(qvn6yanbyk2y^vqh%-*q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

# -------------------------------------------------------
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        # 允许任何用户访问
        'rest_framework.permissions.AllowAny',
        # 允许普通用户访问
        'rest_framework.permissions.IsAuthenticated',
        # 允许超管访问
        'rest_framework.permissions.IsAdminUser',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    )
}

ACC_JUMP = True

CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = (
    '*'
)

CORS_ALLOW_METHODS = (
    'GET',
    'OPTIONS'
    'POST',
    'DELETE',
)

CORS_ALLOW_HEADERS = (
    '*'
)

# -------------------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.homepage',
    'users',
    'apps.hls',
    'zabbix',
    'job_manager',
    'django_celery_results',
    'rest_framework',
    # 'dwebsocket',
    'audit',
    'cmdb_auth',
    # 'accounts',
    'channels',
]

ASGI_APPLICATION = 'cmdb_hls.routing.application'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# WEBSOCKET_ACCEPT_ALL = True   # 可以允许每一个单独的视图实用websockets

ROOT_URLCONF = 'cmdb_hls.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'cmdb_hls.wsgi.application'

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cmdb_hls',
        'HOST': '175.178.121.39',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': 'dkmwebmysql!q$EWQ23FD23',
    }
}

# Password validation
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )
STATICFILES_DIRS = (
    ('css', os.path.join(STATIC_ROOT, 'css').replace('\\', '/')),
    ('js', os.path.join(STATIC_ROOT, 'js').replace('\\', '/')),
    ('vue', os.path.join(STATIC_ROOT, 'vue').replace('\\', '/')),
    ('images', os.path.join(STATIC_ROOT, 'images').replace('\\', '/')),
    ('lib', os.path.join(STATIC_ROOT, 'lib').replace('\\', '/')),
    ('fonts', os.path.join(STATIC_ROOT, 'fonts').replace('\\', '/')),
)

# Default primary key field type
# https://docs.djangoproject.com/en/dev/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.User'

# logging.basicConfig(
#     level=logging.INFO,
#     format='[%(asctime)s %(levelname)s] > %(message)s \n',
#     filename='/data/log/cmdb_hls_log/djangoLog.log',
# )

LOGGING_DIR = "/data/log/cmdb_hls_log/"
if not os.path.exists(LOGGING_DIR):
    os.makedirs(LOGGING_DIR)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,  # 是否禁用logger
    'formatters': {
        # ================format参数中可能用到的格式化字符串=================
        # %(name)s  Logger的名字
        # %(levelno)s   数字形式的日志级别
        # %(levelname)s 文本形式的日志级别
        # %(pathname)s  调用日志输出函数的模块的完整路径名，可能没有
        # %(filename)s  调用日志输出函数的模块的文件名
        # %(module)s    调用日志输出函数的模块名
        # %(funcName)s  调用日志输出函数的函数名
        # %(lineno)d    调用日志输出函数的语句所在的代码行
        # %(created)f   当前时间，用UNIX标准的表示时间的浮 点数表示
        # %(relativeCreated)d   输出日志信息时的，自Logger创建以 来的毫秒数
        # %(asctime)s   字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
        # %(thread)d    线程ID。可能没有
        # %(threadName)s    线程名。可能没有
        # %(process)d   进程ID。可能没有
        # %(message)s   用户输出的消息
        'standard': {
            'format': '[%(levelname)s] [%(asctime)s] [%(name)s] [%(filename)s] [%(funcName)s] [%(lineno)d ] > [%(message)s]'
        },
    },
    # 过滤器，提供给handler使用(可以不使用)，也可以自定义过滤函数
    # 过滤loggers传递给handlers的信息
    'filters': {
        # 过滤debug为True
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    # 处理器，设置日志记录方式
    'handlers': {
        # =================class设置分类（根据需求设置）=================
        # 'logging.StreamHandler'  # 控制台打印
        # 'logging.FileHandler'  # 保存到文件
        # 'logging.handlers.RotatingFileHandler'  # 保存到文件，根据文件大小自动切
        # 'logging.handlers.TimedRotatingFileHandler'  # 保存到文件，根据时间自动切
        # 'django.utils.log.AdminEmailHandler'  # 管理员发送错误电子邮件（）

        'console': {
            'level': 'DEBUG',
            # 'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            # 'class': 'mysite.logger_class.ConsoleHandler',
            'formatter': 'standard'
        },
        'file_handler': {
            'level': 'WARNING',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '%s/cmdb_py2.log' % LOGGING_DIR,
            'maxBytes': 1024 * 1024 * 500,  # 日志大小 500M
            'formatter': 'standard',
            'encoding': 'utf-8',
            'delay': True
        },
        'file_handler_script': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '%s/cmdb_hls_script.log' % LOGGING_DIR,
            # 日志大小 500M
            'maxBytes': 1024 * 1024 * 5,
            'formatter': 'standard',
            'encoding': 'utf-8'
        }
    },
    # 日志记录器
    'loggers': {
        'django': {
            # 一个记录器中可以使用多个处理器
            'handlers': ['console', 'file_handler'],
            'level': 'WARNING',
            'propagate': True,
        },
        'request': {
            'handlers': ['file_handler'],
            'level': 'ERROR',
            'propagate': False,
        },
        'script': {
            'handlers': ['file_handler_script'],
            'level': 'INFO',
            # 是否继承⽗类的log信息
            'propagate': False,
        },
    }
}


# 日志根目录
LOG_BASE_DIR = "/var/log"
# 每一页显示几条
PAGE_SIZE = 10
# 分页数
PAGE_NUM_PAGES = 11
# 服务器ssh端口
SSH_PORT = 22
# 下载日志目录
DOWN_LOG_DIR = "/tmp/log_download"
