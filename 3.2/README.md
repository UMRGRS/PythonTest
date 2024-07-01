## 3.2 Explica qué son los módulos en Python y cómo se utilizan.
Los módulos son archivos que contiene funcionalidad que deseamos incluir a nuestro código, pueden ser clases, funciones, sentencias, etc.
Para incluir un modulo hacemos uso de la sentencia import como se muestra en el ejemplo.
```python
#3.2
#Generador de números aleatorios
import random as rand #Podemos importar los módulos con alias para hacer nuestro código mas legible
#Funciones matemáticas
import math

#Una vez importado podemos hacer uso de la funcionalidad que el modulo provee
#Random
random_number = rand.randint(0, 100)

print('El numero ganador es {}'.format(random_number))

#Math
number = 5

print('El cuadrado de {} es {}'.format(number, math.pow(number, 2)))

print('{} grados es igual {} radianes'.format(number, math.radians(number)))

print('La raíz cuadrada de {} es {}'.format(number,math.sqrt(number)))
```
