'''
Bucles
1. Ejercicio: Imprime los números del 1 al 10 usando un bucle for .
2. Ejercicio: Imprime los números pares del 1 al 20 usando un bucle while .
3. Ejercicio: Usa un bucle para calcular la suma de los números del 1 al 100.
'''
#1
i = 1
for i in range (1, 11 , 1):
  print(i)
  i += 1

#2
x = 0
while x <= 20:
  print(x)
  x += 2

#3
y = 1
res = 0
while y <= 100:
  res +=  y
  y += 1
print("La suma del 1 al 100 es" ,res)


