'''
1. Ejercicio: Dado un número, imprime si es positivo o negativo.
2. Ejercicio: Dado un número, imprime si es par o impar.
3. Ejercicio: Dado tres números, encuentra y muestra el mayor de ellos.
'''
#1
x = 5
if x < 0:
  print("El numero es negativo")
elif x > 0:
  print("El numero es positivo")
else:
  print("El numero es 0")

#2
y = 0
if y % 2==0:
  print("El numero es par")
else:
  print("El numero es impar")

#3
a = 15
b = 50
c = 12
if a < b and c < b:
  print("El numero mas grande es" ,b)
elif b < a and c < a:
  print("El numero mas grande es" ,a)
else:
  print("El numero mas grande es" ,c)
  
