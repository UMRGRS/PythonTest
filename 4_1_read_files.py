#Almacenamos la ruta del archivo que vamos leer
filename = './test_files/datos.txt'

#Abrimos el archivo
data = open(filename)

#Imprimimos en pantalla el contenido con la función read() 
print(data.read())