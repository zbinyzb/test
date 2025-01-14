"""
Django settings for website project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'wkerc8&2jsr^%$^31lroa2!w91ge%4e^h9apvn932tn4#(@@qb'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'channels',
    'blog'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'website.urls'

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

WSGI_APPLICATION = 'website.wsgi.application'
ASGI_APPLICATION = 'website.routing.application'
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1',6379)],
        },
    },
}

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/upload/'
MEDIA_ROOT = os.path.join(BASE_DIR,'upload').replace('\\','/')

# 将允许将cookie包含在跨站点HTTP请求中
CORS_ALLOW_CREDENTIALS = True
# 允许任何网站向您的网站发出跨域请求
CORS_ALLOW_ALL_ORIGINS = True
# 授权进行跨站点HTTP请求的来源列表[白名单]
CORS_ALLOWED_ORIGINS  =  [ 
    'http://127.0.0.1'
]
#允许用户请求的方法
CORS_ALLOW_METHODS = [
    'DELETE' ,
    'GET' ,
    'OPTIONS' ,
    'POST' ,
    'PUT' ,
    'VIEW'
]
#允许的请求头
CORS_ALLOW_HEADERS  =  [ 
    'XMLHttpRequest' ,
    'X_FILENAME',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'orign',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'Pragma'
]


#APPID
# ALIPAY_APPID = "2021002131695584"   #实际应用
ALIPAY_APPID = "2021000117624232"   #沙箱模拟
#网关
ALIPAY_URL = "https://openapi.alipaydev.com/gateway.do"     #沙箱模拟
# ALIPAY_URL = "https://openapi.alipay.com/gateway.do"
#回调地址
# ALIPAY_NOTIFY_URL = "http://zbin.cn/pay_result/"
#前端首页
# ALIPAY_RETURN_URL = "http://blog.study.zbin.cn/"

#使用密钥字符串
#应用公钥
# ALIPAY_PUBLIC_KEY = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAhenJNpUkd5teoENeW4mbdWJoqgEQIZxgmJOLjjjlH5RQRM3DhfFdjJNQzNZjNSmzDt4snIy6B0xSzZ4+53wrSq+uMe/mQqlp6EXusWl8EpmVod/sWxrDmset2vqFoJCIiGISEWSaUEQJLpmPqzU9sSNZnirS2cxZwWSgT//BsWZQrsEAkAAlsdoyBihesk8mE3l9TsyC8grpPpQwLSrpu74pV5EIGmiQ5Ji/FEuMGb1DC0kxl5nwaeu+bqVAcvkMzUynXqBbzB1VES29DcdbH20s/rpLU/EkQOrpDVP6hx9QEGlhCKx3veCbWcbYQ0kJcsp3eCC2Hhy05ur6xHokuQIDAQAB"
#沙箱模拟
ALIPAY_PUBLIC_KEY = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEArvMxi3Jlk806LmyO8a5qZ8fDjGb5uHffqkV/90h6xPXnfYQSQDev3tMmg4vYwM+3XHtydgG2tZQ9SlBzIK2ND04NOx0xN8KJxR/9jWI0oWJ0M/0Sg99d05NZheSUZYTWHcApIO6BYuJXqbvZOJA/IvqQBjCtjudep97fRzv3k3HZjYT1wyKrBrvsNukLH6Tw0FMXZzJmp72J5iQMdfe8vCWy4TmLlNygrz4ACnt+DlwkxgzzLCQkGj2GJOuDbZl1qs2dMER37io77dunIcMd5kWnVuPLf4RXKcuNzgZgq6Izdkj8pvIKZeleOC0qetvv2gTZfmSeVtipHEFDb0iQKQIDAQAB"
#应用私钥
# APP_PRIVATE_KEY = "MIIEowIBAAKCAQEAhenJNpUkd5teoENeW4mbdWJoqgEQIZxgmJOLjjjlH5RQRM3DhfFdjJNQzNZjNSmzDt4snIy6B0xSzZ4+53wrSq+uMe/mQqlp6EXusWl8EpmVod/sWxrDmset2vqFoJCIiGISEWSaUEQJLpmPqzU9sSNZnirS2cxZwWSgT//BsWZQrsEAkAAlsdoyBihesk8mE3l9TsyC8grpPpQwLSrpu74pV5EIGmiQ5Ji/FEuMGb1DC0kxl5nwaeu+bqVAcvkMzUynXqBbzB1VES29DcdbH20s/rpLU/EkQOrpDVP6hx9QEGlhCKx3veCbWcbYQ0kJcsp3eCC2Hhy05ur6xHokuQIDAQABAoIBAHkTNT/KfNw/d8DC6G8u7YWmYidDKsiY0KVi0YzXWCHDQQfUWnGiFwjgsO9i7vPELgbFTeSFQDUVBtCtwQYeuC2gxYiU9MVU01KU2AlD7FAM2MMw6Ew+2Jf67e/NDkBsLWXR9bAQG41y1jJx2Pnc+1hLM93TriwJnSVDy8ZI4WF4Z65evUIFz9EjqJEu/0T4Ss7VoqnhldgCE6xQrVBQSDuLVbCD+opkXtq14rsow5sa0gmC4ebebQr+ysX9x7nTv3RgwcQcAGu2wKGiuOEKsDr8FlepHbfU7lcGwgWRFVaCrkJtOE19byY49CRTnETWn6MxrHkF99t0mdl7581+3pkCgYEAuc+DtueKOvzg2VXzrb9HaCS06HYRv9kaJ7rKPPxPf2gKihjr0MJ2atzlmN14y4+EoRq7sTk1YZeOKuNImvQv3CljK0rnwYctq5Q49tMndN6opj/T8M6dbz8QD4i809nmb1pubmiMIWfvUjhv0HtmUdeqznPHR53a1b/HgbfPUhMCgYEAuH+gpBAnYa+phji0tfp4yj/isCLf+G4UCZyWG2Inh40AHQmivYh1uYpjYU/++OVEY0ITDAoF32zhZGoMoloJ+0hy2Ki7bQTRDhLXeKUC+A3sjaRiNolcApWQZXQo2QhQJN+CkfDd5UgKAVz2WtweUbTH9TeG1ccnH3UE077c54MCgYBxW2YxucQdBJVwQf2trBo2MN6lSxK9Bgfs4QnsdslRIvn7EgUbkOeJfkYcIlFFbsMtPg/vqMUmSr2S8KIk1oA0QpObn9EPwhZcrMqr2loh9IzTD/GO4Z4udjyoHXWFkVQB7xucA/ApmSzp7kBY4k+j8nzkAsI6sNUGvj9Kpga3PQKBgQCA73BsN33OHtzyGB7yLiDL9umM/lJXY1ZNgUjFykqlyDwUDu/UVNEw4S2ijC07871fQIXfHAIOqiC59ALwUsw29+KK1yBkh8ExfKlofqkcgV6XfhHE2ymaBLvsqskBI3YezrSJGTN5UGbtnPHtfXcS0qwLCssICy2kJjtBX1kx0QKBgEojRrGf5vBZtoaeO7jE1m9VbPbjw5v07foyhOkBlRxJXkSjofY5wlix8Q4ryusEAIw8XaWb0WAyjI9/HZWYyi0iZN/5ReM02+qnBqKdinpcPQRSVA3hcCXItJnEeqPS8bwql8YdV7r471JIwSjyCAp74xHg0jOYWUKk6GqMVkR9"
#沙箱模拟
APP_PRIVATE_KEY = "MIIEowIBAAKCAQEArvMxi3Jlk806LmyO8a5qZ8fDjGb5uHffqkV/90h6xPXnfYQSQDev3tMmg4vYwM+3XHtydgG2tZQ9SlBzIK2ND04NOx0xN8KJxR/9jWI0oWJ0M/0Sg99d05NZheSUZYTWHcApIO6BYuJXqbvZOJA/IvqQBjCtjudep97fRzv3k3HZjYT1wyKrBrvsNukLH6Tw0FMXZzJmp72J5iQMdfe8vCWy4TmLlNygrz4ACnt+DlwkxgzzLCQkGj2GJOuDbZl1qs2dMER37io77dunIcMd5kWnVuPLf4RXKcuNzgZgq6Izdkj8pvIKZeleOC0qetvv2gTZfmSeVtipHEFDb0iQKQIDAQABAoIBAD342bEK2d6MUTLGs6/616hhg+yFQapNlEYtjlHbM9n3PYQht5FV6I+m/jqU3DgYnFw/QmF44+7YTwm3C8EkmRY10MwC4D9fQww388oUYo5UYNNVryxVgFgFFy4ttT9s2af6PNd0hRKxGNqAN0cpGaRbW49FyQUZAle2xCLopB9vGWuldroUuv5pqPvX+bDeTRRMRHYsjcNpXKBPbiZiWKeg/i26WDcpiwWTBtUUxSDMRFvToovCl8te4bEVkEiNRC5+LpRq2Lkm8NYTwToca2//GyQQf8upb7JY82JsDUlPuQbJl9K8U7xMUKl809ZB8/Q74trClw2mWjNxZrR4hHECgYEA/i7Ms3kzgwMQ2G/ELGwjwYxsMrFAlsPPAcwZhzaqDVZdovMKpqh6L63CUaRfhdS/JDPU/7DrzdJkfhotRhinMvW6QU3j/EvG76KZc9kAH0+0l/Efkxi8IZg7Oot3i1/AWVncHtum1+SK93sr66vPOUdDFEr8ELNwP73vhGvqva0CgYEAsDNiL7OjKn5wiil5soyk8mjiQ7qCfdu3CqWrN4/Gjjdv+lS1sXbTGEdGU5C7/wtyzH+8nfiLXexKjqzgH2FYlhlMmeJtZPkfKP7HAqqF6G364IpZIp7l0FFdzQUZAlbSPpvUFjIF3PWTDq/jUEOfQ61eIE06xQ8j/+IOdKKTs+0CgYEA10YppmMjBnWFQdm+6uSXj+fvByvqCQZDf0Et6b+ZXHxmB4kR3z5XZaQjLGQrZrxdOjsPzZI40/O5mrdu2qwsh1NocMCYM2i2TuSGVIBXwy0NRZY46KsNQuKcXyQZlhf9X29kp1nev4BXVeyisRGtCtTY8gnj2/0tNz8U6TFA+W0CgYAvPEcpJI4sWSMQVtgSHpQljCqEH57V4K3sQ8dnqLqA66mwQT9IKOOkUY8v3dAYKliHLANDkhrCfhLqtruKjg0yh+u6ITJUbFiHI+3z8ATf74Pe6BfHKTPQqc9so941e1L3h8zOenCJ8KeQu2RD4yzx9qsSG8ISi+GJum9Ho0HXbQKBgEkHn9ipts2V5QJFd2Q1bn4djRtSCGJSSkw82SGmbXOtxGR873J986O29IH3MR9GJCgB1FcP3tMduAKxj6x+mExXSzyb0WjCLfrlfB0Mt5UQFJq0+ftmyhlbMiWxQwdSHRvKEc77IkIsHfAOJptomfmVmLbdykfR9hgxMP/CRewn"