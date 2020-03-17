import requests
from dotenv import load_dotenv
import os
import logging

load_dotenv()
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

base_url = os.getenv('BASE_URL')


class TestCase:

    def test_register(self):
        logger.info('Register test case')
        url = base_url + '/register'
        data = {'username': 'admin20', 'password': 'admin20@123', 'email': 'admin21@gmail.com',
                'image': '/home/admin1/Pictures/image.png'}
        res = requests.post(url=url, data=data)
        logger.info(res.text)
        assert res.status_code

    def test_login(self):
        logger.info('Login test case')
        url = base_url + '/login'
        data = {'email': 'admin16@gmail.com', 'password': 'admin16@123'}
        res = requests.post(url, data=data)
        logger.info(res.text)
        assert res.status_code
