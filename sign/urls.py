from django.urls import include, re_path
from sign import views, views_if

app_name = 'sign'

urlpatterns = [
    # 添加接口
    # guest system interface:
    # ex: /api/add_event/
    re_path('add_event/', views_if.add_evnet, name='add_event'),
    # ex: /api/add_guest/
    re_path('add_guest/', views_if.add_guest, name='add_guest'),
    # ex: /api/get_evnet_list/
    re_path('get_event_list/', views_if.get_event_list, name='get_evnet_list'),
    # ex: /api/get_guest_list/
    re_path('get_guest_list/', views_if.get_guest_list, name='get_guest_list'),
    # ex: /api/user_sign/
    re_path('user_sign/', views_if.user_sign, name='user_sign'),
]
