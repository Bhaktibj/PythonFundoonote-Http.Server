import requests
from setting import FUNDOO
base_url = FUNDOO['base_url']


class TestCase:

    def test_register_valid(self):
        url = base_url + '/register'
        data = {'username': 'admin20', 'password': 'admin20@123', 'email': 'admin21@gmail.com'}
        res = requests.post(url=url, data=data)
        assert res.status_code==200

    def test_register_invalid(self):
        url = base_url + '/register'
        data = {'username': 'admin20', 'password': 'admin20@123', 'email': 'admingmail.com'}
        res = requests.post(url=url, data=data)
        assert res.status_code

    def test_login_valid(self):
        url = base_url + '/login'
        data = {'email': 'admin16@gmail.com', 'password': 'admin16@123'}
        res = requests.post(url, data=data)
        assert res.status_code==200

    def test_login_invalid(self):
        url = base_url + '/login'
        data = {'email': 'admin16@gmail.com', 'password': 'admin16@123'}
        res = requests.post(url, data=data)
        assert res.status_code == 200

    def test_forgot(self):
        url = base_url + '/forgot'
        data = {'email': 'admin16@gmail.com'}
        res = requests.post(url, data=data)
        assert res.status_code ==200

