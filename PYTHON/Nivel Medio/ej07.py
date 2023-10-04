'''
Define una función que tome una cadena y retorne la cantidad de
letras mayúsculas y minúsculas en la cadena.
'''
def may_min(text):
    may = sum(1 for letra in text if letra.isupper())
    min = sum(1 for letra in text if letra.islower())
    return may, min

print(may_min("Buenos Dias"))