'''
Define una función que tome un número y retorne un diccionario con
la tabla de multiplicar de ese número del 1 al 10.
'''
def tab_multiplicar(num):
    return {i: num * i for i in range(1, 11)}


print(tab_multiplicar(7))