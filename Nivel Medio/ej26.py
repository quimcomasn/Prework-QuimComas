'''
Define una función que tome dos listas y retorne la lista de elementos que no están en ambas listas.
'''
def no_comun(list1, list2):
    return list(set(list1) ^ set(list2))

print(no_comun([1,4,5,6],[1,2,3,4]))