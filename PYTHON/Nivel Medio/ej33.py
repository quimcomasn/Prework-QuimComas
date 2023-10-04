'''
Escribe una función que reciba una lista de tuplas y retorne una lista
ordenada basada en el último elemento de cada tupla.
'''
def ordenar_elemento(tuplas):
    return sorted(tuplas, key=lambda x: x[-1])

print(ordenar_elemento([(1,4), (5, 2), (4, 5)]))