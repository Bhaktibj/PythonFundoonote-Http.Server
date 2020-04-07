import requests
from fundoonote.setting import FUNDOO
import pytest
base_url = FUNDOO['base_url']


class TestCase:
    @pytest.fixture
    def test_headers(self):
        headers = {'token':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwiZXhwIjoxNTg1NTY4MTE4fQ.3r6Q-6TmxCzkODo15RXpDXjq4nMAQEW44wnk2AE2Z7E'}
        print(headers)
        return headers

    def test_create_note(self, test_headers):
        """ this test method is used to test the note create api"""
        url = base_url + '/create/note'
        data = {'title': 'second note', 'description': 'this is second note', 'color': 'Green',
                'is_archived': 0, 'is_deleted': 0, 'is_trashed': 0, 'is_restored': 0, 'is_pinned':0}
        res = requests.post(url=url, data=data, headers=test_headers)
        print(res.text)
        assert res.status_code==200

    def test_delete_note(self, test_headers):
        """ this test case is used to test the note delete api"""
        url = base_url + '/delete/note'
        data = {'id': 1} # passing data
        res = requests.delete(url=url, data=data, headers=test_headers)
        assert res.status_code==200 # assert response

    def test_list_note(self, test_headers):
        """ this test case is used to test the list note api"""
        url = base_url + '/list/note'
        res = requests.get(url=url, headers=test_headers)
        assert res.status_code ==200

    def test_get_note(self, test_headers):
        """ this test case is used to test the get note api"""
        url = base_url + '/read/note'
        data = {'id': 1}
        res = requests.post(url=url, data=data, headers=test_headers)
        assert res.status_code == 200