'''
Define una función que reciba una lista de palabras y un entero n,
y retorne la lista de palabras que son más largas que n.
'''
def filtrar(lista, num):
    return [palabra for palabra in lista if len(palabra) > num]

print(filtrar(["buenos", "dias", "buenas", "noches"], 4)) 