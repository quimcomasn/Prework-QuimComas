'''
Define una función que tome dos listas y retorne True si tienen al
menos un miembro en común, de lo contrario, retorne False.
'''
def comun(list1, list2):
    return bool(set(list1) & set(list2))

print(comun([1, 6, 3], [6, 4, 9]))