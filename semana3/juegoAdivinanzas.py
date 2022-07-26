#hacer un juego de adivinanzas
#el numero a adivinar es aleatorio
#entre 0 y 20
#el codigo debe generar automaticamente el aleatorio
#y preguntarle al usuario con un input el numero que quiere adivinar
#el juego debe tener un maximo numero de intentos.
#si me paso del maximo sin adivinar pierdo.  si adivino gano.

import random

def GuessTheNumber(maxRetries,):


    #numero a adivinar:
    numberToGoes = random.randint(0,20)
    #maximo numero de intentos:
    maxGuess = maxRetries
    #contador de intentos del usuario:
    contUserGuess = 0
    #variable a determinar si un usuario gano:
    won = False

    while contUserGuess < maxGuess and not won:
        userInput = int(input("Adivina el número entre 0 y 20: "))
        if userInput == numberToGoes:
            print("Has ganado!")
            won = True
        else:
            print("Respuesta Incorrecta")
            contUserGuess = contUserGuess + 1
            print(f"Te quedan {maxGuess - contUserGuess} intentos")

    if contUserGuess == maxGuess:
        print(f"Has perdido!.  El número a encontrar es {numberToGoes} ")

GuessTheNumber(3)


