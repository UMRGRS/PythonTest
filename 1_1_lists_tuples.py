#Las listas son mutables y se declaran entre corchetes
#Ejemplo de una lista
myList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#Podemos modificar los elementos de la lista libremente
print('Lista original: {}'.format(myList))

myList[0] = myList[-1]

print('Lista modificada: {}'.format(myList))


#Las tuplas en cambio son inmutables y se declaran entre paréntesis
#Ejemplo de una tupla
myTuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

#Si intentamos modificar algún elemento de la tupla obtendremos un error
print('Tupla original: {}'.format(myTuple))

try:
    myTuple[0] = "No es posible"
except Exception as e:
    print('Obtenemos el siguiente error: {}'.format(e))
    
print('La tupla se mantiene sin cambios: {}'.format(myTuple))

