
# todoアプリへのパスを記述

from django.urls import path
from . import views

urlpatterns =[
    # home
    path ('', views.home, name = 'home'),

    # about
    path('about/', views.about, name = 'about'),

    # 削除
    path('delete/<list_id>', views.delete, name="delete"),

    # タスク切り替え
    path('uncomplete/<list_id>', views.uncomplete, name="uncomplete"),
    path('complete/<list_id>', views.complete, name="complete"),
]
