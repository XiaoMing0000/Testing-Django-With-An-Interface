from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from sign.models import Event, Guest
from django.shortcuts import render, get_object_or_404


# Create your views here.
# 创建首页
def index(request):
    return render(request, 'index.html')


# 登录动作
def login_action(request):
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)  # 登录
            response = HttpResponseRedirect('/event_manage')
            # response.set_cookie('user', username, 3600)  # 添加浏览器 cookie
            request.session['user'] = username  # 将 session 信息记录到浏览器
            return response
        else:
            return render(request, 'index.html', {'error': 'username or password error!'})


# 账号说明
# 账号                  密码
# admin                 admin
# xiaoming0001          gongshengnan01

# 发布会管理
# @login_required  # 显示某个试图函数必须登录才能访问
def event_manage(request):
    # username = request.COOKIES.get('user', '')          # 读取浏览器 cookie
    event_list = Event.objects.all()
    username = request.session.get('user', '')  # 读取浏览器 session
    return render(request, 'event_manage.html', {"user": username, "events": event_list})


# 发布会名称搜索
# @login_required
def search_name(request):
    username = request.session.get('user', '')
    get_search_name = request.GET.get("name", "")
    event_list = Event.objects.filter(name__contains=get_search_name)
    return render(request, 'event_manage.html', {'user': username, 'events': event_list})


# @login_required
def guest_manage(request):
    username = request.session.get('user', '')
    guest_list = Guest.objects.all()

    # 分页
    paginator = Paginator(guest_list, 10)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    return render(request, 'guest_manage.html', {'user': username, 'guests': contacts})


# @login_required
# def search_realname(request):
#     username = request.session.get('user')
#     get_search_name = request.GET.get('name', '')
#     guest_list = Guest.objects.filter(realname__contains=get_search_name)
#     # 分页
#     paginator = Paginator(guest_list, 2)
#     page = request.GET.get('page')
#     try:
#         contacts = paginator.page(page)
#     except PageNotAnInteger:
#         # If page is not an integer, deliver first page.
#         contacts = paginator.page(1)
#     except EmptyPage:
#         # If page is out of range (e.g. 9999), deliver last page of results.
#         contacts = paginator.page(paginator.num_pages)
#
#     return render(request, 'guest_manage.html', {'user': username, 'guests': contacts})


# @login_required
def search_phone(request):
    username = request.session.get('user')
    get_search_name = request.GET.get('name', '')
    guest_list = Guest.objects.filter(phone__contains=get_search_name)
    # 分页
    paginator = Paginator(guest_list, 2)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    return render(request, 'guest_manage.html', {'user': username, 'guests': contacts})


# 签到页面
@login_required
def sign_index(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'sign_index.html', {'event': event})


# 签到动作
# @login_required
def sign_index_action(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    phone = request.POST.get('phone', '')
    result = Guest.objects.filter(phone=phone)
    if not result:
        return render(request, 'sign_index.html', {'event': event, 'hint': 'phone error.'})
    result = Guest.objects.filter(phone=phone, event_id=event_id)
    if not result:
        return render(request, 'sign_index.html', {'event': event, 'hint': 'event id or phone error.'})
    result = Guest.objects.get(phone=phone, event_id=event_id)
    if result.sign:
        return render(request, 'sign_index.html', {'event': event, 'hint': "user has sign in."})
    else:
        Guest.objects.filter(phone=phone, event_id=event_id).update(sign='1')
    return render(request, 'sign_index.html', {'event': event, 'hint': 'sign in success!', 'guest': result})


# 退出登录
@login_required
def logout(request):
    auth.logout(request)  # 退出登录
    response = HttpResponseRedirect('index')
    return response
