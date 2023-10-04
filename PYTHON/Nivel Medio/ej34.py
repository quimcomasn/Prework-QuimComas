'''
Define una función que reciba una cadena y retorne la cantidad de
letras vocales en la cadena.
'''
def contar_vocales(text):
    return sum(1 for c in text.lower() if c in 'aeiou')

print(contar_vocales("Buenos dias"))