import unittest
import requests


class GetEventListTest(unittest.TestCase):
    ''' 查询发布会信息'''

    def setUp(self):
        self.base_url = 'http://127.0.0.1:8000/api/sec_get_event_list/'
        self.auth_user = ('admin', 'admin')

    def test_get_event_list_null(self):
        ''' auth 为空 '''
        r = requests.get(self.base_url, params={'eid': ''})
        self.assertEqual(result['status'], 10011)
        self.assertEqual(result['message'], 'user auth null')

    def test_get_evnet_list_auth_error(self):
        ''' auth 错误'''
        r = requests.get(self.base_url, auth=('abc', '123'), params={'eid': '1'})
        result = r.json()
        self.assertEqual(result['status'], 10012)
        self.assertEqual(result['message'], 'user auth fail')

    def test_guest_event_list_eid_null(self):
        ''' eid 为空'''
        r = requests.get(self.base_url, auth=self.auth_user, params={'eid': ''})
        result = r.json()
        self.assertEqual(result['status'], 10021)
        self.assertEqual(result['message'], 'parameter error')

    def test_guest_event_list_eid_success(self):
        ''' eid 为空'''
        r = requests.get(self.base_url, auth=self.auth_user, params={'eid': '1'})
        result = r.json()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['data']['name'], '红米 Pro 发布会')
        self.assertEqual(result['data']['maximum'], 2000)
        self.assertEqual(result['data']['status'], True)
        self.assertEqual(result['data']['address'], '北京会展中心')
        self.assertEqual(result['data']['start_time'], '2023-08-20T14:00:00')
