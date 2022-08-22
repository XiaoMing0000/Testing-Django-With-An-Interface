from django.test import TestCase
from sign.models import Event, Guest
from django.test.utils import setup_test_environment
from django.test import Client
from django.contrib.auth.models import User
from datetime import datetime


# Create your tests here.
class ModelTest(TestCase):
    def setUp(self):
        Event.objects.create(id=1, name='oneplus 3 event', status=True, limit=2000,
                             address='shenzhen', start_time='2022-08-31 12:00:00')
        Guest.objects.create(id=1, event_id=1, realname='alen',
                             phone='13711001101', email='alen@mail.com', sign=False)

    def test_event_models(self):
        result = Event.objects.get(name='oneplus 3 event')
        self.assertEqual(result.address, 'shenzhen')
        self.assertTrue(result.status)

    def test_guest_models(self):
        result = Guest.objects.get(phone='13711001101')
        self.assertEqual(result.realname, 'alen')
        self.assertFalse(result.sign)


# 测试
class IndexPageTest(TestCase):
    ''' 测试 index 登录首页 '''

    def setUp(self):
        setup_test_environment()

    def test_index_page_renders_index_template(self):
        ''' 测试 index 试图 '''
        response = self.client.get('/index/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


class LoginActionTest(TestCase):
    ''' 测试登录函数 '''

    def setUp(self):
        User.objects.create_user('admin', 'admin@mail.com', 'admin123456')
        self.c = Client()

    def test_login_action_username_password_null(self):
        ''' 登录名密码为空 '''
        test_data = {'username': '', 'password': ''}
        response = self.c.post('/login_action/', data=test_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'username or password error!', response.content)

    def test_login_action_username_password_error(self):
        ''' 用户名密码错误 '''
        test_data = {'username': 'abc', 'password': '123'}
        response = self.c.post('/login_action/', data=test_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'username or password error!', response.content)

    def test_login_action_success(self):
        ''' 登录成功 '''
        test_data = {'username': 'admin', 'password': 'admin'}
        response = self.c.post('/login_action/', data=test_data)
        self.assertEqual(response.status_code, 302)


# 发布会管理
class EventManageTest(TestCase):
    ''' 发布会关闭 '''

    def setUp(self):
        Event.objects.create(id=2, name='xiaomi5', limit=2000, status=True,
                             address='beijing', start_time=datetime(2035, 8, 10, 16, 0, 0))
        self.c = Client()

    def test_event_manage_success(self):
        ''' 测试发布会： xiaomi5 '''
        response = self.c.post('/event_manage/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'xiaomi5', response.content)
        self.assertIn(b'beijing', response.content)

    def test_event_manage_search_success(self):
        ''' 测试发布会搜索 '''
        response = self.c.post('/search_name/', {'name': 'xiaomi5'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'xiaomi5', response.content)
        self.assertIn(b'beijing', response.content)
