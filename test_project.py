from python import crear, listado, eliminar_files, listar_recientes
from flask import Flask, abort, request

import requests

def test_create():
	r= requests.post('http://localhost:6969/files', json={"filename":"funciona", "content":"funciona"})
	r=crear()
	assert r==201


