'''
Define una función que tome un número y calcule su serie de Fibonacci.
'''

def serie(num):
    if num <= 0:
        return []
    elif num == 1:
        return [0]
    fib = [0, 1]
    while len(fib) < num:
        fib.append(fib[-1] + fib[-2])
    return fib


print(serie(8))