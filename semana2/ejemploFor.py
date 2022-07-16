#Calcular promedio de esta lista

listOfNumber = [-10, 50, 800, 9, 6, 23.5]
#Calculamos elementos de la lista
#print(len(listOfNumber))
cont = 0
for element in listOfNumber:
    cont = cont + 1
print("el total de elementos de la lista es: ", cont)

suma = 0
for element in listOfNumber:
    suma = suma + element
print("la suma de los elementos en la lista es ",suma)
print("el promedio de los datos es: ", suma/cont )