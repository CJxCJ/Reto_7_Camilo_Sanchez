#se declaran
x = 1
y = 0

while x <= 1000 :
  x += 1
  if x%2 != 0:
    continue
  print(x)

while y <= 999 :
  y += 1
  if y%2 == 0:
    continue
  print(y)