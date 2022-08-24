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
from django.urls import include, re_path
from django.contrib import admin
from django.urls import path
from sign import views, views_if

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),  # 添加  index/ 路径配置
    path('accounts/login/', views.index),  # 设置 accounts/login 登录页面映射到 index 页面
    # path 说明， index: localhost:8000:index,  views.index： 访问的函数
    path('login_action/', views.login_action),  # 登录检测
    path('event_manage/', views.event_manage),  # 登录成功后的跳转的页面
    path('search_name/', views.search_name),  # 搜索功能
    path('guest_manage/', views.guest_manage),  # 嘉宾表单
    path('search_phone/', views.search_phone),  # 嘉宾表单搜索
    re_path(r'^sign_index/(?P<event_id>[0-9]+)/$', views.sign_index),  # 签到页面
    re_path('sign_index_action/(?P<event_id>[0-9]+)/$', views.sign_index_action),  # 签到事件
    path('logout/', views.logout),  # 退出系统

    # 配置接口路径，当所有接口都已经开发完成，需要配置接口的访问路径
    re_path(r'^api', include('sign.urls', namespace='sign')),

    # 添加接口
    # guest system interface:
    # ex: /api/add_event/
    re_path(r'^/add_event/', views_if.add_evnet, name='add_event'),
    # ex: /api/add_guest/
    re_path(r'^/add_guest/', views_if.add_guest, name='add_guest'),
    # ex: /api/get_evnet_list/
    re_path(r'^/get_event_list/', views_if.get_evnet_list, name='get_evnet_list'),
    # ex: /api/get_guest_list/
    re_path(r'^/get_guest_list/', views_if.get_guest_list, name='get_guest_list'),
    # ex: /api/user_sign/
    re_path(r'^/user_sign/', views_if.user_sign, name='user_sign'),
]
