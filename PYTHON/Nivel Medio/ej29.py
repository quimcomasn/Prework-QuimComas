'''
Define una función que reciba una lista de números y retorne el pro
medio de los números en la lista.
'''
def promedio(list):
    return sum(list) / len(list)

print(promedio([2,5,9,10,3]))