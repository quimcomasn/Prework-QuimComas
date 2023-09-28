'''
Define una función que reciba una cadena y cuente el número de dígi
tos y letras que contiene.
'''
def contar(text):
    digitos = sum(i.isdigit() for i in text)
    letras = sum(i.isalpha() for i in text)
    return digitos, letras

print(contar("25 aniversario"))