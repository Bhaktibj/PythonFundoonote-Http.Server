import requests
from fundoonote.setting import FUNDOO
base_url = FUNDOO['base_url']


class TestCase:

    def test_create_note(self):
        """ this test method is used to test the note create api"""
        url = base_url + '/create/note'
        headers = {'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MywiZXhwIjoxNTg0OTU1OTg1fQ.svZpsg4eW0VGiPHD7kP6j2e5FfIMFq8guZRSSSjNnPg'}
        data = {'title': 'second note', 'description': 'this is second note', 'color': 'Green',
                'is_archived': 0, 'is_deleted': 0, 'is_trashed': 0, 'is_restored': 0, 'is_pinned':0}
        res = requests.post(url=url, data=data, headers=headers)
        print(res.text)
        assert res.status_code==200

    def test_delete_note(self):
        """ this test case is used to test the note delete api"""
        url = base_url + '/delete/note'
        headers = {'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MywiZXhwIjoxNTg0OTU1OTg1fQ.svZpsg4eW0VGiPHD7kP6j2e5FfIMFq8guZRSSSjNnPg'} # passing headers for login required
        data = {'id': 1} # passing data
        res = requests.post(url=url, data=data, headers=headers)
        assert res.status_code==200 # assert response

    def test_list_note(self):
        """ this test case is used to test the list note api"""
        url = base_url + '/list/note'
        headers = {'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MywiZXhwIjoxNTg0OTU1OTg1fQ.svZpsg4eW0VGiPHD7kP6j2e5FfIMFq8guZRSSSjNnPg'} # token
        res = requests.get(url=url, headers=headers)
        assert res.status_code ==200

    def test_get_note(self):
        """ this test case is used to test the get note api"""
        url = base_url + '/read/note'
        headers = {'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MywiZXhwIjoxNTg0OTU1OTg1fQ.svZpsg4eW0VGiPHD7kP6j2e5FfIMFq8guZRSSSjNnPg'}
        data = {'id': 1}
        res = requests.post(url=url, data=data, headers=headers)
        assert res.status_code == 200

