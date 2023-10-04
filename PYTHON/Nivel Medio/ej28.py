'''
Define una función que reciba un número entero positivo y retorne la
suma de los cuadrados de todos los números pares menores o iguales a ese número.
'''
def suma_cuadrados(num):
    return sum(i**2 for i in range(2, num+1, 2) )

print(suma_cuadrados(10))