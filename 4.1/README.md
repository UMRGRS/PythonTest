## 4.1 Escribe un programa en Python que lea el contenido de un archivo llamado datos.txt y lo imprima por pantalla.
```python
#4.1
#Almacenamos la ruta del archivo que vamos leer
filename = './test_files/datos.txt'

#Abrimos el archivo
data = open(filename)

#Imprimimos en pantalla el contenido con la función read() 
print(data.read())
```
