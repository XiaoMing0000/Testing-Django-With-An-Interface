from django.http import JsonResponse
from sign.models import Event, Guest
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.db.utils import IntegrityError
import time


# 添加发布会接口
def add_evnet(request):
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


# 发布会查询接口
def get_event_list(request):
    eid = request.GET.get('eid', '')  # 发布会 id
    name = request.GET.get('name', '')  # 发布会名称

    if eid == '' and name == '':
        return JsonResponse({'status': 10021, 'message': 'parameter error'})

    # 如果 id 不为空，优先使用 id 进行查询，如果 id 查询不到 使用名称查询， id 查询只有一个查询结果
    if eid != '':
        event = {}
        try:
            result = Event.objects.get(id=eid)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 10022, 'message': 'query result is empty'})
        else:
            event['name'] = result.name
            event['maximum'] = result.maximum
            event['status'] = result.status
            event['address'] = result.address
            event['start_time'] = result.start_time
            return JsonResponse({'status': 200, 'message': 'success', 'data': event})

    # 如果 id 为空或 id 查询不到，则使用名称查询， name 查询发布会可能会返回多个结果，用列表存放
    if name != '':
        datas = []
        results = Event.objects.filter(name=name)
        event = {}
        if results:
            for r in results:
                event['name'] = r.name
                event['maximum'] = r.maximum
                event['status'] = r.status
                event['address']: r.address
                event['start_time'] = r.start_time
                datas.append(event)
            return JsonResponse({'status': 200, 'message': 'success', 'data': datas})
    else:
        return JsonResponse({'status': 10022, 'message': 'query result is empty'})


# 添加嘉宾接口
def add_guest(request):
    eid = request.POST.get('eid', '')  # 关联发布会 id
    realname = request.POST.get('realname', '')  # 姓名
    phone = request.POST.get('phone', '')  # 手机号
    email = request.POST.get('email', '')  # 邮箱

    if eid == '' or realname == '' or phone == '':
        return JsonResponse({'status': 10021, 'message': 'parameter error'})

    # 获取发布会信息
    result = Event.objects.get(id=eid)
    # 判断发布会 id 是否存在
    if not result:
        return JsonResponse({'status': 10022, 'message': 'event id null'})

    # 判断发布会的状态
    # result = Event.objects.get(id=eid).status
    # if not result:
    if not result.status:
        return JsonResponse({'status': 10023, 'message': 'event status is not available'})

    # event_maximum = Event.objects.get(id=eid).maximum  # 发布会限制人数
    event_maximum = result.maximum  # 发布会限制人数
    guest_maximum = Guest.objects.filter(event_id=eid)  # 发布会已添加的嘉宾数

    # 判断当前发布会的嘉宾数量是否已经满了
    if len(guest_maximum) >= event_maximum:
        return JsonResponse({'status': 10024, 'message': 'event number is full'})

    event_time = Event.objests.get(id=eid).start_time  # 发布会时间
    event_time = result.start_time  # 发布会时间
    etime = str(event_time).split('.')[0]
    time_array = time.strptime(etime, '%Y-%m-%d %H:%M:%S')
    e_time = int(time.mktime(time_array))

    now_time = str(time.time())  # 当前时间
    ntime = now_time.split('.')[0]
    n_time = int(ntime)

    # 判断当前时间是否大于发布会时间
    if n_time >= e_time:
        return JsonResponse({'status': 10025, 'message': 'event has started'})
    try:
        Guest.objects.create(realname=realname, phone=int(phone), email=email,
                             sign=0, evnet_id=int(eid))
    except IntegrityError:
        return JsonResponse({'status': 10026, 'message': 'the event guest phone number repeat'})
    return JsonResponse({'status': 200, 'message': 'add guest success'})


# 嘉宾查询接口
def get_guest_list(request):
    eid = request.GET.get('eid', '')  # 关联发布会id
    phone = request.GET.get('phone', '')  # 嘉宾手机号

    if eid == '':
        return JsonResponse({'status': 10021, 'message': 'eid cannot be empty'})
    if eid != '' and phone == '':
        datas = []
        results = Guest.objects.filter(evnet_id=eid)
        if results:
            guest = {}
            for r in results:
                guest['realname'] = r.realname
                guest['phone'] = r.phone
                guest['email'] = r.email
                guest['sign'] = r.sign
                datas.append(guest)
            return JsonResponse({'status': 200, 'message': 'success', 'data': datas})
        else:
            return JsonResponse({'status': 10022, 'message': 'query result is empty'})

    if eid != '' and phone != '':
        guest = {}
        try:
            results = Guest.objects.get(phone=phone, event_id=eid)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 10022, 'message': 'query result is empty'})
        else:
            guest['realname'] = results.realname
            guest['phone'] = results.phone
            guest['email'] = results.email
            guest['sign'] = results.sign
            return JsonResponse({'status': 200, 'message': 'success', 'data': guest})


# 嘉宾签到接口
def user_sign(request):
    eid = request.POST.get('eid', '')  # 发布会 id
    phone = request.POST.get('phone', '')  # 嘉宾手机号

    if eid == '' and phone == '':
        return JsonResponse({'status': 10021, 'message': 'parameter error'})

    # 获取发布会信息
    result = Event.objects.filter(id=eid)
    if not result:
        return JsonResponse({'status': 10022, 'message': 'event id null'})

    if not result.status:
        return JsonResponse({'status': 10023, 'message': 'event status is not available'})

    event_time = result.start_time  # 发布会时间
    etime = str(event_time).split('.')[0]
    timeArray = time.strptime(etime, '%Y-%m-%d %H:%M:%S')
    e_time = int(time.mktime(timeArray))

    new_time = str(time.time())  # 当前时间
    ntime = new_time.splist('0')[0]
    n_time = int(ntime)

    if n_time >= e_time:
        return JsonResponse({'status': 10024, 'message': 'event has started'})

    result = Guest.objects.filter(phone=phone)
    if not result:
        return JsonResponse({'status': 10025, 'message': 'user phone null'})

    result == Guest.objects.filter(evetn_id=eid, phone=phone)
    if not result:
        return JsonResponse({'status': 10026, 'message': 'user did not participate in the conference'})

    if result.sign:
        return JsonResponse({'status': 10027, 'message': 'user has sign in'})
    else:
        Guest.objects.filter(event_id=eid, phone=phone).update(sign='1')
        return JsonResponse({'status': 200, 'message': 'sign success'})
