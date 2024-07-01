#2.2
#Modulo para generar números aleatorios
import random as rand

spell = rand.randint(1,4)

if(spell == 1):
    print('You cast fireball!. Everyone, including you takes 10 damage.')
elif(spell == 2):
    print('You cast light. Better run.')
elif(spell == 3):
    print('You cast protection. At least you are protected for one turn.')
else:
    print("You've run out of mana. Well, you can still bonk things with your catalyst")