from python import crear, listado, eliminar_files, listar_recientes
import flask

app = Flask(__name__)
app.test_request_context('/?filename=Pete&content=estavainafunciona')


#def func(x):
#   return x + 1

#def test_answer():
#    assert func(3) == 5

def test_crear():
    assert crear()== 201
=======
#def func(x):
#    return x + 1
#
#def test_answer():
#    assert func(4) == 5

def test_crear():
    assert crear()== 400
>>>>>>> c090a33cfa8ac003cd7108b878a029ccf95989eb
