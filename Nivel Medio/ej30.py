'''
Define una función que reciba una lista de cadenas y retorne la cadena 
más larga en la lista.
'''
def cadena_larga(list):
    return max(list, key=len)

print(cadena_larga(["hola", "adios", "noches"]))