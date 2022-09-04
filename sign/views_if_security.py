# 签名加时间戳
import hashlib
import time
from django.http import JsonResponse
from sign.models import Event
from django.core.exceptions import ValidationError, ObjectDoesNotExist


def user_sign(request):
    client_time = request.POST.get('time', '')
    client_sign = request.POST.get('sign', '')
    if client_time == '' or client_sign == '':
        return 'sign null'

    # 服务器时间
    now_time = time.time()
    # server_time = str(int(now_time))
    server_time = str(now_time).split('.')[0]
    # 获取时间差
    time_difference = int(server_time) - int(client_time)
    if time_difference >= 60:
        return 'timeout'

    # 签名检查
    md5 = hashlib.md5()
    sign_str = client_time + '&Guest-Bugmaster'
    sign_bytes_utf8 = sign_str.encode(encoding='utf-8')
    md5.update(sign_bytes_utf8)
    server_sign = md5.hexdigest()
    if server_sign != client_sign:
        return 'sign error'
    else:
        return 'sign right'


# 添加发布会接口 --- 增加签名+时间戳
def add_event(request):
    sign_result = user_sign(request)  # 调用签名函数
    if sign_result == 'sign null':
        return JsonResponse({'status': 10011, 'message': 'user sign null'})
    elif sign_result == 'timeout':
        return JsonResponse({'status': 10012, 'message': 'user sign timeout'})
    elif sign_result == 'sign error':
        return JsonResponse({'status': 10013, 'message': 'user sign error'})

    eid = request.POST.get('eid', '')  # 发布会id
    name = request.POST.get('name', '')  # 发布会标题
    maximum = request.POST.get('maximum', '')  # 限制人数
    status = request.POST.get('status', '')  # 状态
    address = request.POST.get('address', '')  # 地址
    start_time = request.POST.get('start_time', '')  # 发布会时间

    # 判断用户信息是否为空
    if eid == '' or name == '' or maximum == '' or address == '' or start_time == '':
        return JsonResponse({'status': 10021, 'message': 'parameter error'})

    # 判断会议 ID 是否已经存在
    result = Event.objects.filter(id=eid)
    if result:
        return JsonResponse({'status': 10022, 'message': 'event id already exists'})

    # 杨正发布会名称是否存在
    result = Event.objects.filter(name=name)
    if result:
        return JsonResponse({'status': 10023, 'message': 'event name already exists'})

    # 如果用户没有设置发布会状态，给发布会设置一个初始状态
    if status == '':
        status = 1

    try:
        # 创建发布会
        Event.objects.create(id=eid, name=name, maximum=maximum, address=address,
                             status=int(status), start_time=start_time)
    except ValidationError as e:
        # 如果验证错误返回提示格式信息
        error = 'start_time format error. It must be in YYYY-MM-DD HH:MM:SS format.'
        return JsonResponse({'status': 10024, 'message': error})
    return JsonResponse({'status': 200, 'message': 'add event success'})


# 演示时间戳的使用
if __name__ == '__main__':
    now_time = time.time()
    print('当前时间戳：' + str(now_time))

    # 转换成日期格式
    otherStyleTime = time.strftime(
        '%Y-%m-%d %H:%M:%S', time.localtime(now_time))
    print('日期格式：' + str(otherStyleTime))
