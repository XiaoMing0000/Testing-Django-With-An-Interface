from django.urls import include, re_path
from sign import views, views_if, views_if_sec
from django.urls import path

app_name = 'sign'

urlpatterns = [
    # 添加接口
    # guest system interface:
    # ex: /api/add_event/
    path('add_event/', views_if.add_evnet),
    # ex: /api/add_guest/
    path('add_guest/', views_if.add_guest),
    # ex: /api/get_evnet_list/
    path('get_event_list/', views_if.get_event_list),
    # ex: /api/get_guest_list/
    path('get_guest_list/', views_if.get_guest_list),
    # ex: /api/user_sign/
    path('user_sign/', views_if.user_sign),

    # ex: /api/sec_get_evnet_list/
    path('sec_get_event_list/', views_if_sec.get_event_list),  # 嘉宾表单搜索
]
