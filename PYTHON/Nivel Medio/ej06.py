'''
Define una función que tome una lista y un número n, y retorne los
primeros n elementos de la lista
'''
def primer_n(list, num):
    return list[:num]

print(primer_n([1,3,5,7,9],4))