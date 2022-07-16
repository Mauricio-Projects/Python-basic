#Paso1 : pedirle al usuario la cantidad de personas a ingresar.

#paso2: un for de las 0 a N personas y pedir las edades de esas N personas.

#paso3: guardar las edades de esas personas en una lista.

#paso4: calcular el promedio de esas personas.

numberOfPersons =  int(input("Por favor ingrese la cantidad de personas: "))

listOfAges = []

for i in range(0, numberOfPersons):
    listOfAges.append(int(input("Por favor ingrese la edad de la persona: ")))

average = sum(listOfAges) / len(listOfAges)
print(f"El promedio de las edades es {average} años")