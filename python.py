from flask import Flask
from comandos import get_all_files, eliminar_archivos, get_recientes


app = Flask(__name__)
api_url = '/files'

@app.route(api_url,methods=['POST'])
def crear():
  content = request.get_json(silent=True)
  nombre= content['filename']
  contenido= content['content']
  if not nombre or not contenido:
  	return "no es posible crear el archivo", 400
  if nombre in get_all_files():
  	return "se sobreescribió el archivo"
  return "archivo creado exitosamente", 200


@app.route(api_url,methods=['GET'])
def listado():
  list = {}
  list["files"] = get_all_files()
  return json.dumps(list), 200

@app.route(api_url,methods=['DELETE'])
def eliminar_archivos():
  eliminar_todo()
  return "todos los archivos fueron eliminados", 200


@app.route(api_url+"/recently_created",methods=['GET'])
def listar_recientes():
  list = {}
  list["reciente"] = get_recientes()
  return json.dumps(list), 200


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080,debug='True')