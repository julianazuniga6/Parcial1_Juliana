from python import crear, listado, eliminar_files, listar_recientes
from flask import Flask, abort, request

app = Flask(__name__)
app.test_request_context('/?filename=Pete&content=estavainafunciona')


#def func(x):
#   return x + 1

#def test_answer():
#    assert func(3) == 5

def test_crear():
    assert crear()== 201
#def func(x):
#    return x + 1
#
#def test_answer():
#    assert func(4) == 5


