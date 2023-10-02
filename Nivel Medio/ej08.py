'''
Define una función que tome un número y retorne True si es unnúmero perfecto, False en caso contrario. 
Un número perfecto es aquel que es igual a la suma de sus divisores propios positivos. 
Por ejemplo, 6 es un número perfecto porque sus divisores son 1, 2 y 3, y 6 = 1 + 2 + 3
'''
def es_perfecto(num):
    return num == sum(divisor for divisor in range(1, num) if num % divisor == 0)

print(es_perfecto(6))