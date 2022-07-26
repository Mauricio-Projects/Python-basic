#hacer un juego de piedra papel o tijera contra el computador.
#el computador escoge aleatoriamente: piedar, papel o tijera.
#pedir al usuario su input
#el juego debe terminar cuando alguno de los dos gane 2 de 3 partidas.

from platform import machine
import random
from unittest import result

#funcion para que el computador escoja piedra, papel o tijera.
def machineSelection():
    randomNumber = random.randint(1,3)
    if randomNumber == 1:  #1 = a Rock
        return "R"
    elif randomNumber == 2: # 2 = Paper
        return "P"
    elif randomNumber == 3: # 3 = Scissor
        return "S"

def evaluateRoickPaperScissorConditions(machine, user):
    if machine ==  user:
        return "Empate"

    if machine == "R" and user == "S":
        return "machine"
    elif user == "R" and machine == "S":
        return "user"
    
    if machine == "P" and user == "R":
        return "machine"
    elif user == "P" and machine == "R":
        return "user"
    
    if machine == "S" and user == "P":
        return "machine"
    elif user == "S" and machine == "P":
        return "user"
    
def playRockPaperScissor():
    contMachine = 0
    contUser = 0


    while contMachine < 2 and contUser < 2 :
        machine = machineSelection()
        user = input("Please, enter your selection (R, P, S): ")
        result = evaluateRoickPaperScissorConditions(machine, user)
        if result == "machine":
            contMachine = contMachine + 1
            print("La maquina Gana")
        elif result == "user":
            contUser = contUser + 1
            print("El usuario Gana")
        else:
            print("Empate")

    if contMachine == 2:
        return "machine"
    elif contUser == 2:
        return "user"

winner = playRockPaperScissor()
print ("el ganador definitivo es: ", winner)