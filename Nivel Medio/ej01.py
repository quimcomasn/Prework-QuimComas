'''
Ejercicio: Define una función que utilice un bucle para imprimir los primeros números de la serie de Fibonacci.
'''
def fib(num):
    x, y = 0, 1
    for i in range(num):
        print(x, end=" ")
        x, y= y, x + y

fib(8)
