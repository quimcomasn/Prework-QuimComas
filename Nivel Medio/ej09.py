'''
Define una función que reciba un número y retorne su representación
en binario.
'''
def binario(num):
    return bin(num).replace("0b", "")

print(binario(5))