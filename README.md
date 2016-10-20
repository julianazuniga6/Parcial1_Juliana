## Parcial #1 de Sistemas Operativos  
### Juliana Zúñiga, código 13207011

### Implementación y despliegue de servicios web en un explorador haciendo uso de Flask

1.	Crear un ambiente virtual en el directorio deseado  
```bash
$ virtualenv flask_environment
```  
Se creará un directorio con el nombre flask_environment  
2.	Para activar el ambiete ejecutar el comando
```bash
$ . /flask_environment/bin/activate
```
3.  Instalar Flask con el ambiente activo:
```bash
     (flask_environment) $ pip install Flask
```
4.	He decidido desplegar mi servicio en el puerto 6969, por tanto se debe modificar el archivo iptables. Para ello, ejecutar:
```bash
vi /etc/sysconfig/iptables.
```
  Cuando se muestre el contenido de iptables se debe añadir la línea:  
  `-A INPUT -p tcp -m state --state NEW -m tcp --dport 6969 -j ACCEPT`  
  Es importante añadirla antes de la línea que contiene:  
  `-A INPUT -j REJECT --reject-with icmp-host-prohibited`
5.  Se debe reiniciar el servicio iptables  
```bash  
$ service iptables restart 
```  
6.  Para desplegar el servicio web para las URI __/files__ y __/files/recently_created___, crer un archivo *.py que soporte las peticiones HTTP que se requieren: __POST, GET__ y __DELETE__.

  El archivo __python.py__ que adjunto permite: listar todos los archivos, borrar todos los archivos y crear un nuevo archivo en el directorio __/home/filesystem_user/files/__

```python
#python.py
from flask import Flask, abort, request
from comandos import get_all_files, eliminar_a, get_recientes, create_file
import json


  app = Flask(__name__)
  api_url = '/files'

  @app.route(api_url,methods=['POST'])
  def crear():
    content = request.get_json(silent=True)
    nombre= content['filename']
    contenido= content['content']
    resp= create_file(nombre, contenido)
    if not nombre:
     return "no es posible crear el archivo", 400
    else:
      return resp, 201


  @app.route(api_url,methods=['GET'])
  def listado():
    list = {}
    list["files"] = get_all_files()
    return json.dumps(list), 200

  @app.route(api_url,methods=['DELETE'])
  def eliminar_files():
    for file in get_all_files():
      eliminar_a(file)
    return "HTTP 200 OK- SE ELIMINARON LOS ARCHIVOS DE filesystem_user", 200


  @app.route(api_url+"/recently_created",methods=['GET'])
  def listar_recientes():
    list = {}
    list["files"] = get_recientes()
    return json.dumps(list), 200


  if __name__ == "__main__":
      app.run(host='0.0.0.0',port=6969,debug='True')
```
  Los comandos que se ejecutan desde python para poder implementar las funcionalidades del script anterior se muestran en ___comandos.py___

```python
#comandos.py
from subprocess import Popen, PIPE

def get_all_files():
	lista = Popen(["ls","/home/filesystem_user/files/"], stdout=PIPE, stderr=PIPE).communicate()[0].split('\n')
	return filter(None,lista)

def create_file(filename, content):
	create= Popen(["touch", "/home/filesystem_user/files",filename])
	a=open("/home/filesystem_user/files/"+filename,"w")
	a.write(content)
	a.close()
	return "HTTP 201 CREATED- se creo el archivo"


def eliminar_a(file):
	r=Popen(["rm", '-f', "/home/filesystem_user/files/"+file], stdout=PIPE, stderr=PIPE)

	return "se han eliminado todos los archivos de filesystem_user"


def get_recientes():
	lista= Popen(["find", "/home/filesystem_user/files/", '-type', 'f', '-mtime', '-1'], stdout=PIPE, stderr=PIPE)
	#recientes= Popen(["grep", "filesystem_user/files/"], stdin=lista.stdout, stdout=PIPE, stderr=PIPE).communicate()[0].split('\n')
	listo= Popen(["awk", '-F', '/', '{print $5}'], stdin=lista.stdout, stdout=PIPE, stderr=PIPE).communicate()[0].split('\n')
	return filter(None,listo)
```

Por ultimo, ejecutar el archivo __python.py__ y el servicio estará listo para responder a las peticiones que se hagan desde POSTMAN. LAs capturas de pantalla que muestran este servicio web en funcionamiento se muestran a continuación.
```bash  
(flask_environment) $ python python.py 
```


![alt text](https://s9.postimg.org/gxmgya1hb/listar.png "Listar todos los archivos")

![alt text](https://s9.postimg.org/4t77haolb/crear.png "Crear nuevo archivo")

![alt text](https://s9.postimg.org/b868dyvb3/eliminar.png "Eliminar archivos")

![alt text](https://s9.postimg.org/nclhuy873/recientes.png "Mostrar archivos recientes")

El repositorio en __GitHub__ que contiene los archivos de pythonse encuentra en https://github.com/julizuoso/Parcial1_Juliana
