'''
Define una función que reciba una lista de números y retorne la suma 
acumulada de los números
'''

def suma_lista(list):
    total = 0
    suma = []
    for numero in list:
        total += numero
        suma.append(total)
    return suma

print(suma_lista([1,35,50,10,5]))