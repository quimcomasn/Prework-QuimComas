'''
Define una función que tome una cadena y retorne un diccionario con
la cantidad de apariciones de cada caracter en la cadena.
'''

def contar(text):
    return {caracter: text.count(caracter) for caracter in text}

print(contar("coca cola"))