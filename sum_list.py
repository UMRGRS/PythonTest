#3.1
#ASCII
numbers = [104, 105, 114, 101, 32, 109, 101, 32, 112, 108, 101, 97, 115, 101]

def suma_lista(number_list):
    add = 0
    for number in number_list:
        add += number
    return add
        
print('La suma de los elementos es {}'.format(suma_lista(numbers)))