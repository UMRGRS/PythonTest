## 6.1 Explica qué es una clase en Python y cómo se define.
Una clase es un tipo de plantilla o molde para crear objetos que contienen atributos y funcionalidad, pero cuyos valores pueden variar. 
Una clase en Python se define con la palabra clave class seguida del nombre de la clase y dos puntos.
```python
#6.1
#Creamos la clase con la palabra clave class
class VideoGame():
    #Definimos el constructor con los atributos de la clase
    def __init__(self, name, publisher, year):
        self.name = name
        self.publisher = publisher
        self.year = year
        
    #Podemos definir funciones para que todos los objetos creados las utilicen
    def PrintData(self):
        print('Nombre {}'.format(self.name))
        print('Publicado por {}'.format(self.publisher))
        print('Año {}'.format(self.year))
        
#A partir de la clase podemos crear multiples objetos con distintos atributos

destiny = VideoGame(name='Destiny', publisher='Activision', year=2014)
minecraft = VideoGame(name='Minecraft', publisher='Mojang', year=2009)
osu = VideoGame(name='OSU', publisher='ppy', year=2007)

#Cada objeto puede llamar al método PrintData
destiny.PrintData()
print('------------')
minecraft.PrintData()
print('------------')
osu.PrintData()
```
