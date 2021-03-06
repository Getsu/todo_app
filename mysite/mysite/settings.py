"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

from dotenv import load_dotenv
load_dotenv()
# print(load_dotenv())


# プロジェクト内にパスを作成
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# 秘密鍵
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')
# print(SECRET_KEY)



# デバッグモードの有効化
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# リリース時は公開するサイトのドメイン名（*.example.com）を入れる
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles', # ↑デフォルトのアプリ
    'todo.apps.TodoConfig', # todoアプリを作成するため追記
]


# 有効化するMiddlewareクラス（リクエスト/レスポンス処理にhookを加えるための仕組み）
# HTTP 要求を受け取ったり、HTTP 応答を返却する際に、ここで定義したミドルウェアを順次実行
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ルートディレクトリの設定(モジュールでどの設定を使うか指定)
# /.mysite/urls.py を指定
ROOT_URLCONF = 'mysite.urls'

# テンプレートに関する定義
# BACKEND: テンプレートエンジン
# DIRS: テンプレートを探す対象のフォルダリスト
# APP_DIRS: アプリケーションフォルダは以下を探すか否かの札ぐ
# OPTIONS: 各種オプション情報
# context_processors: テンプレートで参照可能な変数を生成するプロセッサ群
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

# WSGI のアプリケーションを指定
# 下記の場合は ./mysite/wsgi.py の application を指定
WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
# データベースに関する定義
# SQLite3, MySQL(MariaDB), PostgresSQL, Oracle など利用可能
# sqlite3を選択し、./db.sqlite3に生成
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators
# パスワードの禁止ルールを指定
# ユーザ名と似たパスワード、パスワード長、よくあるパスワード、数値のみのパスワードをチェック
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
# デフォルトの言語を指定

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'ja-JP' # 日本語と英語を選択

# タイムゾーン
# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Tokyo' # タイムゾーンを東京に変更

# 多言語機能を有効にするか否かを指定 (I18N:Internationalisation)
USE_I18N = True

# 日付フォーマットなどのどーから胃ゼーション機能を有効にするかどうかを指定
# L10N: localization
USE_L10N = True

# タイムゾーン変換機能を有効にするか否かを指定
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
# スタティックファイル (CSS, JHavaScript, Images) のURLを指定
STATIC_URL = '/static/'

# Add
STATICFILES_DIR = [
    os.path.join(BASE_DIR, 'static'),
]
