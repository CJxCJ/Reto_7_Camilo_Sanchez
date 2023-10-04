#se importa la funcion ramdom
import random

#se define la funcion de adivinar
def adivina():
    print("Piensa en un número entre 1 y 100 :D")
    minimo = 1
    maximo = 100
    
    #se declara un ciclo verdadero
    while True:
        #se declara una variable aleatoria 
        x = random.randint(minimo, maximo)
        
        #se le pide al usuario que reponda segundo 
        print("tu número es " + str(x))
        print("( responde 'igual' si es correcto, 'menor' si es menor, 'mayor' si es mayor):")
        respuesta = input()
        
        #dependiendo de la respuesta del usuario hacer algunos de los condicionales
        if respuesta == 'igual':
            print("Adiviné tu número")
            break
        elif respuesta == 'menor':
            maximo = x - 1
        elif respuesta == 'mayor':
            minimo = x + 1
        else:
            print("Por favor, responde 'igual', 'menor' o 'mayor'.")

#se termina el ciclo
adivina()

