'''
Define una función que reciba una lista de números y retorne el
segundo número más grande de la lista.
'''
def segundo_max(list):
    return sorted(set(list), reverse=True) [1]


print(segundo_max([1,35,50,10,5]))