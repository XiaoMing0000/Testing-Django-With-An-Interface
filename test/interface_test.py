import requests
import unittest


class GetEventListTest(unittest.TestCase):
    ''' 查询发布会接口测试 '''

    def setUp(self):
        self.url = 'http://127.0.0.1:8000/api/get_event_list'

    def test_get_event_null(self):
        '''  发布会 id 为空 '''
        r = requests.get(self.url, params={'eid': ''})
        result = r.json()
        print(result)
        self.assertEqual(result['status'], 10021)
        self.assertEqual(result['message'], 'parameter error')

    def test_get_evnet_success(self):
        ''' 正确查询 '''
        r = requests.get(self.url, params={'eid': '1'})
        result = r.json()
        print(result)
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'success')
        self.assertEqual(result['data']['name'], '中国中心发布会')
        self.assertEqual(result['data']['limit'], 10000)
        self.assertEqual(result['data']['status'], True)
        self.assertEqual(result['data']['address'], '中国中心')
        self.assertEqual(result['data']['start_time'], '2022-07-26T02:42:48')
