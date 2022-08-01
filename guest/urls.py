"""guest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from sign import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),              # 添加  index/ 路径配置
    path('accounts/login/', views.index),       # 设置 accounts/login 登录页面映射到 index 页面
    # path 说明， index: localhost:8000:index,  views.index： 访问的函数
    path('login_action/', views.login_action),      # 登录检测
    path('event_manage/', views.event_manage),      # 登录成功后的跳转的页面
]
