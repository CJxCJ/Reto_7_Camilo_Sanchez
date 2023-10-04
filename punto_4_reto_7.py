#se definen las variables de la poblacion y el año de inicio
A = float(25)
B = float(18.5)
C = 2022

#mientras la poblacion de
while A > B:
  porcentajeA = (1 + 0.02)
  porcentajeB = (1 + 0.03)
  A *= porcentajeA
  B *= porcentajeB
  C +=1
print(C)
