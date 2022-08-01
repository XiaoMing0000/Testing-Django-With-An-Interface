from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required


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
@login_required         # 显示某个试图函数必须登录才能访问
def event_manage(request):
    # username = request.COOKIES.get('user', '')          # 读取浏览器 cookie
    username = request.session.get('user', '')  # 读取浏览器 session
    return render(request, 'event_manage.html', {"user": username})
