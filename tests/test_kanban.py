import pytest
from kanban.db import get_db


def test_redirect(client):
    ''' Base ('/') address redirects to  ('/main')'''
    response = client.get('/')
    assert response.headers['Location'] == 'http://localhost/main'

def test_main(client, auth):
    ''' When the user is logged in, they can log out and see the test task.'''
    auth.login()
    response = client.get('/main')
    assert b"Log Out" in response.data
    assert b'test task' in response.data
