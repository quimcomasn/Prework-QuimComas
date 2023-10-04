'''
Define una función que reciba dos listas y retorne la intersección de
ambas (los elementos que están en las dos listas).
'''

def interseccion(list1, list2):
    return list (set(list1) & set(list2))

print(interseccion([1, 6, 3,10], [6, 4, 9,10]))