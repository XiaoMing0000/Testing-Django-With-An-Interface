# 1. 发布会接口

## 无用户验证

| 名称 | 添加发布会 |
| :-- | :-- |
| 描述 | 添加发布会 |
| URL| <http://127.0.0.1:8000/api/add_event/>|
| 调用方式 | POST |
| 传入参数 | eid # 发布会 id</br>name # 发布会标题</br>limit # 限制人数</br>status # 状态</br>address # 地址</br>start_time # 发布会时间 （
2016-08-10 12:00:00） |
| 返回值| {'status':200,</br>'message':'add event success'</br>} |
| 状态 | 码 每一个状态码要有一条用例。</br>{'status':10021,'message':'parameter error'}</br>{'status':10022,'message':'event id already exists'}</br>{'status':10023,'message':'event name already exists'}</br>{'status':10024,'message':'start_time format error. It must be in YYYY-MM-DD HH:MM:SS format.'}</br>{'status':200,'message':'add event success'} |
| 说明 | |

---

# 2. 添加嘉宾接口

| 名称 | 添加嘉宾接口|
| :-- | :-- |
| 描述 | 添加嘉宾接口|
| URL| <http://127.0.0.1:8000/api/add_guest/>|
| 调用方式 | POST|
| 传入参数 | eid # 关联发布会 id </br>realname # 姓名 </br>phone # 手机号 </br>email # 邮箱|
| 返回值| {</br>'status':200, </br>'message':'add guest success' </br>} |
| 状态码| {'status':10021,'message':'parameter error'} </br>{'status':10022,'message':'event id null'} </br>{'status': 10023,'message':'event status is not available'} </br>{'status':10024, message':'event number is full'} </br>{'status':10025,'message':'event has started'} </br>{'status':10026,'message':'the event guest phone number repeat'} </br>{'status':200,'message':'add guest success'} |
| 说明 | |

## 添加签名

| 名称 | 添加嘉宾接口|
| :-- | :-- |
| 描述 | 添加嘉宾接口|
| URL| <http://127.0.0.1:8000/api/add_guest/>|
| 调用方式 | POST|
| 传入参数 | eid # 关联发布会 id </br>realname # 姓名 </br>phone # 手机号 </br>email # 邮箱|
| 返回值| {</br>'status':200, </br>'message':'add guest success' </br>} |
| 状态码| {'status':10011,'message':'user sign null'} </br>{'status':10012,'message':'user sign timeout'} </br>{'status': 10013,'message':'user sign error'} </br>{'status':10021,'message':'parameter error'} </br>{'status':10022,'message':'event id null'} </br>{'status': 10023,'message':'event status is not available'} </br>{'status':10024, message':'event number is full'} </br>{'status':10025,'message':'event has started'} </br>{'status':10026,'message':'the event guest phone number repeat'} </br>{'status':200,'message':'add guest success'} |
| 说明 | |

# 3.查询发布会接口

| 名称     | 查询发布会接口                                               |
| :------- | ------------------------------------------------------------ |
| 描述     | 查询发布会接口                                               |
| URL      | <http://127.0.0.1:8000/api/get_event_list/>                    |
| 调用方式 | GET                                                          |
| 传入参数 | eid #发布会 id </br>name #发布会名称                         |
| 返回值   | {</br>"data": {</br>"start_time": "2016-12-10T14:00:00",</br>"name": "小米手机 6 发布会",</br>"limit": 2000,</br>"address": "北京水立方",</br>"status": true</br>},</br>"message": "success",</br>"status": 200</br>} |
| 状态码   | {'status':10021,'message':'parameter error'}</br>{'status':10022, 'message':'query result is empty'}</br>{'status':200, 'message':'success', 'data':datas} |
| 说明     | eid 或 name 两个参数二选一                                   |

# 4. 查询嘉宾接口

| 名称 | 查询嘉宾接口 |
| :-- | :-- |
| 描述 | 查询嘉宾接口 |
| URL | <http://127.0.0.1:8000/api/get_guest_list/> |
| 调用方式 | GET |
| 传入参数 | eid # 关联发布会 id </br>phone # 嘉宾手机号 |
| 返回值 | {</br>"data": [</br>{</br>"email": "david@mail.com",</br>"phone": "13800110005",</br>"realname": "david",</br>"sign": false</br>},</br>{</br>"email": "david@mail.com",</br>"phone": "13800110005",</br>"realname": "david",</br>"sign": false</br>},</br>{</br>"email": "david@mail.com",</br>"phone": "13800110005",</br>"realname": "david",</br>"sign": false</br>}</br>],</br>"message": "success",</br>"status": 200</br>} |
| 状态码 | {'status':10021,'message':'eid cannot be empty'}</br>{'status':10022, 'message':'query result is empty'}</br>{'status':200, 'message':'success', 'data':datas} |
| 说明 | |

# 5. 嘉宾签到接口

| 名称 | 嘉宾签到接口 |
| :-- |:-- |
| 描述 | 嘉宾签到接口 |
| URL | <http://127.0.0.1:8000/api/user_sign/> |
| 调用方式 | GET |
| 传入参数 | eid # 发布会 id</br>phone # 嘉宾手机号 |
| 返回值 | {</br>'status':200,</br>'message':'sign success'</br>} |
| 状态码 | {'status':10021,'message':'parameter error'}</br>{'status':10022,'message':'event id null'}</br>{'status': 10023,'message':'event status is not available'}</br>{'status':10024,'message':'user phone null'}</br>{'status': 10025,'message':'user did not participate in the conference'}</br>{'status':10026,'message':'user has sign in'}</br>{'status':200,'message':'sign success'} |
| 说明 | |
