'''
Define una función que reciba un número entero y retorne True si es
un número primo, de lo contrario retorne False.
'''

def primo(numero): 
  if numero <= 1: 
    return False 
  for i in range(2, numero): 
    if numero % i == 0: 
      return False 
  return True 

print(primo(15))