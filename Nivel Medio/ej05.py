'''
Define una función que tome una cadena y cuente el número de
vocales en la cadena.
'''
def count(text):
    return sum(1 for letra in text if letra.lower() in "aeiou")

print(count("Buenos dias"))