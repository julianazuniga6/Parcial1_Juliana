import pytest
import python

@pytest.fixture
def client(request):
    client = python.app.test_client()
    return client

def get_files(client):
	return client.get('/files',follow_redirects=True)

def test_get_users(client):
	result = get_files(client)
	assert b'operativos' in result.data


