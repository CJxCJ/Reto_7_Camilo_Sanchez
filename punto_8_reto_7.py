#hacemos una funcion para definir cuando es primo un numero
def primos(x):
  if x <= 1:
    return False
  elif x <= 3:
    return True
  elif x % 2 == 0 or x % 3 == 0:
    return False
  
  i = 5
  while i * i <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return False
        i += 6
  return True

print("Números primos del 1 al 100:")
for n in range(1, 101):
    if primos(n):
        print(n)