'''
Define una función que reciba un número entero n y retorne una lista
con los n primeros números primos
'''
def es_primo(n):
    if n <= 1: 
        return False 
    for i in range(2, n): 
        if n % i == 0:
            return False 
    return True 

def primeros(n):
    primos = []
    num = 1
    while len(primos) < n:
        if es_primo(num):
            primos.append(num)
        num += 1
    return primos

print(primeros(7))
