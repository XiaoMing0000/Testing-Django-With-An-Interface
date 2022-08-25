import requests

# 查询发布会接口
url = 'http://127.0.0.1:8000/api/get_event_list'
r = requests.get(url, params={'eid': '1'})
result = r.json()
print(result)
assert result['status'] == 200
assert result['message'] == 'success'
assert result['data']['name'] == '中国中心发布会'
assert result['data']['limit'] == 10000
assert result['data']['status'] == True
assert result['data']['address'] == '中国中心'
assert result['data']['start_time'] == '2022-07-26T02:42:48'
