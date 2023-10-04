#se decaclara la variable para ingresar un numero
x = int(input("Ingresa un número entre 2 y 50: "))

#si 
if 2 <= x <= 50:
    print("Los divisores de son:" + str(x))
    
    divisor = 1
    

    while divisor <= x:
        if x % divisor == 0:
            print(divisor)
        divisor += 1
else:
    print("El número debe estar en el rango de 2 a 50.")
