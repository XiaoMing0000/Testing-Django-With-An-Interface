import hashlib
import os
import sys
import time
import unittest
import requests
from pyrequest.db_fixture.test_data import init_data

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

from db_fixture import test_data


class AddEventTest(unittest.TestCase):
    ''' 添加发布会 '''

    def setUp(self):
        self.base_url = 'http://127.0.0.1:8000/api/add_event/'

    def tearDown(self):
        print(self.result)

    def test_add_event_all_null(self):
        ''' 所有参数为空 '''
        payload = {'eid': '', '': '', 'maximum': '', 'address': '', 'start_time': ''}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10021)
        self.assertEqual(self.result['message'], 'parameter error')

    def test_add_event_eid_exist(self):
        ''' id 已存在 '''
        payload = {'eid': '1', 'name': '季度发布会', 'maximum': '2000', 'address': '深圳四季交流中心', 'start_time': '2023'}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10022)
        self.assertEqual(self.result['message'], 'event id already exists')

    def test_add_event_name_exist(self):
        ''' id 已存在 '''
        payload = {'eid': '12', 'name': '红米 Pro 发布会', 'maximum': '2000', 'address': '深圳四季交流中心', 'start_time': '2023'}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10023)
        self.assertEqual(self.result['message'], 'event name already exists')

    def test_add_event_data_type_error(self):
        ''' id 已存在 '''
        payload = {'eid': '13', 'name': '季度发布会1', 'maximum': '2000', 'address': '深圳四季交流中心', 'start_time': '2023'}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10024)
        self.assertEqual(self.result['message'], 'start_time format error. It must be in YYYY-MM-DD HH:MM:SS format.')

    def test_add_event_success(self):
        ''' id 已存在 '''
        payload = {'eid': '11', 'name': '季度发布会', 'maximum': '2000', 'address': '深圳四季交流中心',
                   'start_time': '2023-08-28 12:00:00'}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['message'], 'add event success')


class SecAddEventTest(unittest.TestCase):
    def setUp(self):
        # 初始化接口数据
        init_data()
        self.base_url = 'http://127.0.0.1:8000/api/sec_add_event/'
        # app_key
        self.api_key = '&Guest-Bugmaster'
        # 当前时间
        new_time = time.time()
        self.client_time = str(new_time).split('.')[0]
        # sign
        md5 = hashlib.md5()
        sign_str = self.client_time + self.api_key
        sign_byte_utf8 = sign_str.encode(encoding='utf-8')
        md5.update(sign_byte_utf8)
        self.sign_md5 = md5.hexdigest()

    def test_add_event_sign_null(self):
        ''' 签名参数为空 '''
        payload = {'eid': 1, 'maximum': '', 'address': '', 'start_time': '', 'time': '', 'sign': ''}
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        self.assertEqual(result['status'], 10011)
        self.assertEqual(result['message'], 'user sign null')

    def test_add_event_time_out(self):
        ''' 请求超时 '''
        now_time = str(int(self.client_time) - 63)
        payload = {'eid': 1, 'maximum': '', 'address': '', 'start_time': '', 'time': '', 'sign': 'abc',
                   'time': now_time}
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        self.assertEqual(result['status'], 10012)
        self.assertEqual(result['message'], 'user sign timeout')

    def test_add_event_sign_errot(self):
        ''' 签名错误 '''
        payload = {'eid': 1, 'maximum': '', 'address': '', 'start_time': '', 'time': '', 'sign': 'abc',
                   'time': self.client_time}
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        self.assertEqual(result['status'], 10013)
        self.assertEqual(result['message'], 'user sign error')

    def test_add_event_success(self):
        ''' id 已存在 '''
        payload = {'eid': '11', 'name': '季度发布会', 'maximum': '2000', 'address': '深圳四季交流中心',
                   'start_time': '2023-08-28 12:00:00', 'time': self.client_time, 'sign': self.sign_md5}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['message'], 'add event success')


if __name__ == '__main__':
    test_data.init_data()
    unittest.main()
