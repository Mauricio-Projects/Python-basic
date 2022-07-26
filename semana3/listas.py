import random
from xml.dom.minidom import Element

#Hcer una funcion que reciba un numero N 
#y devuelva la lista con N numero aleatorios
#entre 0 y 100

def BuildListOfRandomNumbers(amountOfRandomNumbers, inferiorRange, superiorRange ):
    listOfRandomNumbers = []
    for randomNumber in range(0,amountOfRandomNumbers):
        listOfRandomNumbers.append(random.randint(inferiorRange, superiorRange))
    return listOfRandomNumbers

#buscar si un numero X esta dentro de una lista random.
#si esta,  devolver su posicion en el index.
def searchNumberInRandomList(numberToFind, listToSearch):
    found = False
    for index, element in enumerate(listToSearch):
        if element == numberToFind:
            return element, index
    return found


randomList = BuildListOfRandomNumbers(10, 0, 100)
found = searchNumberInRandomList(17,randomList)
print(randomList)
print(found)