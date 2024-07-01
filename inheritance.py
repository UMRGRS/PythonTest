#6.2
#Imaginemos que desarrollamos un videojuego.
#Todos los personajes tiene atributos y métodos comunes, 
#por lo que creamos una clase como la siguiente.
class Character():
    def __init__(self, health, speed, armor):
        self.health = health
        self.speed = speed
        self.armor = armor
        
    def ShowStats(self):
        print('Salud: {}, Velocidad: {}, Armadura: {}'.format(self.health, self.speed, self.armor))
        
#Dentro del juego pueden existir diferentes clases por ejemplo un hechicero
#que ademas de todas las características de un personaje tiene una lista de hechizos

#Para heredar simplemente colocamos el nombre de la clase padre (Character) entre los paréntesis
class Wizard(Character):
    def __init__(self, health, speed, armor, spells):
        self.spells = spells
        #Llamamos al constructor padre para ahorrar código
        super().__init__(health, speed, armor)
        
    #Definimos un método exclusivo de la clase Wizard
    def ShowSpells(self):
        for spell in self.spells:
            print(spell)
        
#A partir de ahora todas las instancias de Wizard podrán utilizar los atributos y métodos de Character ademas de los propios

blueWizard = Wizard(5, 10, 2, ['Waterfall', 'Cast light',])

blueWizard.ShowStats()

blueWizard.ShowSpells()