'''
Define una función que reciba una cadena y retorne la misma cadena
pero con las palabras en orden inverso.
'''
def invertir(list):
    return ' '.join(reversed(list.split()))

print(invertir("Hola, buenos dias!"))