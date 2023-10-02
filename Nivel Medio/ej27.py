'''
Define una función que tome una lista y retorne la lista sin duplicados.
'''
def no_dup(list1):
    return list(set(list1))

print(no_dup([1,2,3,4,5,2,3,4]))