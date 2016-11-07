import pytest
import python
import json

@pytest.fixture
def client(request):
    client = python.app.test_client()
    return client

def get_files(client):
	return client.get('/files',follow_redirects=True)

def test_get_files(client):
	result = get_files(client)
	assert b'200' in result

def create_file(client):
	return client.post('/files',data=json.dumps(dict(filename='test_file',content='It is working')),content_type='application/json')

def test_create_file(client):
	result= create_file(client)
	assert b'201' in result

def delete_files(client):
	return client.delete('/files',follow_redirects=True)

def test_delete_files(client):
	result= delete_files(client)
	assert b'200' in result 
