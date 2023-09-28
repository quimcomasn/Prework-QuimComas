'''
Ejercicio: Define una función que tome un número y retorne la suma de sus dígitos.
'''
def suma_digitos(n): 
    suma = 0
    while n > 0:
        dig = n % 10
        suma += dig
        n //= 10
    return suma

print(suma_digitos(1451))
