'''
Funciones
1. Ejercicio: Define una función que tome dos números y retorne su suma.
2. Ejercicio: Defineuna función que tome un número y retorne su factorial.
3. Ejercicio: Define una función que tome un número y determine si es primo.
4. Ejercicio: Define una función que reciba una lista de números y retorne la suma de ellos.
5. Ejercicio: Define una función que reciba una cadena de texto y retorne la cadena en reversa.
'''
#1
def suma(n1, n2):
  print(n1 + n2)
suma(10, 15)

#2
def factorial(n):
  if n == 0:
      return 1
  else:
    return n * factorial(n - 1)
print(factorial(10))

#3
def primo(numero): 
  if numero <= 1: 
    return False 
  for i in range(2, numero): 
    if numero % i == 0: 
      return False 
  return True 

if primo(43): 
  print("Es primo") 
else: print("No es primo")

#4
def suma_list(nums):
  total = 0
  for suma in nums:
    total += suma
  return total

print(suma_list([1,3,5,7,9]))

#5
def reversed(text):
  return text[::-1]

print(reversed("ordenador"))