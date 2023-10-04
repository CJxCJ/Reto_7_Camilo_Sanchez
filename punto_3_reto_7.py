#se difine una variable float
x = float(input("ingrese un numero: "))

#mientras x sea mayor a 2
print(x)
while x > 2:
  x -= 1
  if x%2 != 0:
    continue
  print(x)