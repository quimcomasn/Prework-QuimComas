'''
Define una función que encuentre el elemento más común en una lista.
'''
from collections import Counter

def comun(lista):
    return Counter(lista).most_common(1)[0][0]

print(comun([1, 2, 4, 2, 4, 2, 5]))