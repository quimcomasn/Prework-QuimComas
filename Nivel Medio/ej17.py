'''
Define una función que reciba un número y retorne la suma de sus dígitos al cubo.
'''

def suma_digitos(n): 
    suma = 0
    while n > 0:
        dig = n % 10
        suma += dig
        n //= 10
    return suma **3

print(suma_digitos(1451))