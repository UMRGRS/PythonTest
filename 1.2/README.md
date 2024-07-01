## 1.2 ¿Qué es la indexación negativa en Python? Da un ejemplo de cómo se utiliza.
Colecciones de elementos como las listas o las tuplas pueden ser accedidos iniciando desde el final en lugar desde el principio, 
por ejemplo -1 se refiere al último elemento de la colección.
```python
#1.2
"""
Podemos usar indices negativos para facilitar multiples 
tareas como renombrar archivos para darles un identificador
"""
#Modulo para crear identificadores aleatorios
from uuid import uuid4

def RenameFile(filename):
    #La función split convierte un string a una lista, podemos usar el indice -1 para acceder al ultimo elemento y en consecuencia conocer la extension del archivo
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid4().hex, ext)
    return filename

filename = 'Archivo_importante.txt'

print('Archivo original: {}'.format(filename))

filename = RenameFile(filename)

print('Archivo renombrado: {}'.format(filename))
```
