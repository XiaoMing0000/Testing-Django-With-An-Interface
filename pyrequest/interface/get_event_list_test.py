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
        result = r.json()
        self.assertEqual(result['status'], 10011)
        self.assertEqual(result['message'], 'user auth null')

    def test_get_evnet_list_auth_error(self):
        ''' auth 错误'''
        r = requests.get(self.base_url, auth=('abc', '123'), params={'eid': '1'})
        print(r)
        result = r.json()
        self.assertEqual(result['status'], 10012)
        self.assertEqual(result['message'], 'user auth fail')
