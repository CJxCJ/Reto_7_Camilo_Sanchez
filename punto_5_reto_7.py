#se declara que factorial es 1
factorial = 1

#se declara la variable para introducir un numero
x = int(input("Introduzca el número: "))

#se declara i para generar el conteo
i = 1

#mientras i sea menor que x 
while (i <= x):
    #se reealiza la 
    factorial = factorial * i
    i = i + 1

print ("El factorial de " + str(x) + " es " + str(factorial))
    