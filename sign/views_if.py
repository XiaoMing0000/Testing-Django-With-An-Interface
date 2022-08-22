from django.http import JsonResponse
from sign.models import Event
from django.core.exceptions import ValidationError


# 添加发布会接口
def add_evnet(request):
    eid = request.POST.get('eid', '')  # 发布会id
    name = request.POST.get('name', '')  # 发布会标题
    limit = request.POST.get('limit', '')  # 限制人数
    status = request.POST.get('status', '')  # 状态
    address = request.POST.get('address', '')  # 地址
    start_time = request.POST.get('start_time', '')  # 发布会时间

    # 判断用户信息是否为空
    if eid == '' or name == '' or limit == '' or address == '' or start_time == '':
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
        Event.objects.create(id=eid, name=name, limit=limit, address=address,
                             status=int(status), start_time=start_time)
    except ValidationError as e:
        # 如果验证错误返回提示格式信息
        error = 'start_time format error. It must be in YYYY-MM-DD HH:MM:SS format.'
        return JsonResponse({'status': 200, 'message': error})
    return JsonResponse({'status': 200, 'message': 'add event success'})
