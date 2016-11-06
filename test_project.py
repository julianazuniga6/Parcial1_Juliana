from python import crear, listado, eliminar_files, listar_recientes

def test_crear():
    assert crear()== "HTTP 201 CREATED- se creo el archivo", 201
