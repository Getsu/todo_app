from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import List

# 管理画面からデータベースのテーブルを確認できるようにする
admin.site.register(List)
