import base64
from django.contrib import auth as django_auth
import hashlib
from django.http import JsonResponse
from sign.models import Event, Guest
from django.core.exceptions import ValidationError, ObjectDoesNotExist


# 用户认证
def user_auth(request):
    get_http_aut = request.META.get('HTTP_AUTHORIZATION', b'')
    auth = get_http_aut.split()
    try:
        auth_parts = base64.b64decode(auth[1].decode('iso-8859-1')).partition(':')
    except IndexError:
        return 'null'
    userid, password = auth_parts[0], auth_parts[2]
    user = django_auth.authenticate(username=userid, password=password)
    if user is not None and user.is_active:
        django_auth.login(request, user)
        return 'success'
    else:
        return 'fail'


# 发布会查询接口 --- 增加用户认证
def get_event_list(request):
    # 用户认证函数
    auth_result = user_auth(request)
    if auth_result == 'null':
        return JsonResponse({'status': 10011, 'message': 'user auth null'})
    if auth_result == 'fait':
        return JsonResponse({'status': 10012, 'message': 'user auth fail'})

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
