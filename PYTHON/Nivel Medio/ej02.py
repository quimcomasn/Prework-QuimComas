'''
Ejercicio: Define una función que tome un número y retorne una lista de sus divisores.
'''
def divisores(num):
    #for i in range(1, num + 1):
    #     if num % i == 0:
    #         return i      
    
    return [i for i in range(1, num + 1) if num % i == 0]  

print(divisores(10))