import requests
from fundoonote.setting import FUNDOO

base_url = FUNDOO['base_url']


class TestCase:
    """ This test class is used test all user test cases"""

    def test_register_valid(self):
        url = base_url + '/register'
        data = {'first_name': 'admin', 'last_name': 'admin20', 'email': 'admin2gmail.com'}
        res = requests.post(url=url, data=data)
        print(res.text)
        assert res.status_code == 200

    def test_register_invalid(self):
        url = base_url + '/register'
        data = {'first_name': 'admin20', 'last_name': 'admin@123', 'password': '', 'email': 'admingmail.com'}
        res = requests.post(url=url, data=data)
        print(res.text)
        assert res.status_code

    def test_login_valid(self):
        url = base_url + '/login'
        data = {'email': 'nikita.pawar005@gmail.com', 'password': 'nikita123'}
        res = requests.post(url, data=data)
        print(res.text)
        assert res.status_code == 200

    def test_login_invalid(self):
        url = base_url + '/login'
        data = {'email': 'admin16@gmail.com', 'password': 'admin16@123'}
        res = requests.post(url, data=data)
        assert res.status_code == 200

    # def test_forgot(self):
    #     url = base_url + '/forgot'
    #     headers = {
    #         'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwiZXhwIjoxNTg0OTc1MzU4fQ.S0T0A8dozmD2DSHEqqwlcGdrt_kMNBLXfPHEWf6BT_0'}
    #     data = {'email': 'nikita.pawar005@gmail.com'}
    #     res = requests.post(url, data=data, headers=headers)
    #     assert res.status_code == 200
