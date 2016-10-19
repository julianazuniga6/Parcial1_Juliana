from subprocess import Popen, PIPE
from datetime import datetime, timedelta
 
def get_all_files():
	lista = Popen(["ls","/home/filesystem_user"], stdout=PIPE, stderr=PIPE).communicate()[0].split('\n')
	return filter(None,lista)

def create_file(filename, content):
	create= Popen(["vi",filename])

  
def eliminar_archivos():
	elim= Popen(["rm *"], , stdout=PIPE, stderr=PIPE)


def get_recientes():
lista= Popen(["find", "/home/filesystem_user", "-type", "f", "-mtime" "-24"]stdout=PIPE, stderr=PIPE)
recientes= Popen(["grep", "/home/filesystem_user/"]stdin=lista.stdout, stdout=PIPE, stderr=PIPE).communicate()[0].split('\n')
return filter(None,recientes)

	#find /etc -type f -mtime -1



