import pytest
import python

@pytest.fixture
def client(request):
    client = python.app.test_client()
    return client

def get_files(client):
	return client.get('/files',follow_redirects=True)

def test_get_files(client):
	result = get_files(client)
<<<<<<< HEAD
	assert b'200' in result.data
=======
	assert b'nuevo' in result.data

>>>>>>> d6187cec39c35a065bf4543e9d570af8c167db57

def create_file(client):
	response= client.post('/files', data=json.dumps(dict(filename = 'test_file', content= 'Archivo creado desde la prueba')), content_type='application/json')
	assert b'201' in result.data
