
listOfGrades = [
    1,
    2.4,
    4.5,
    2.4,
    4.3,
    3.8,
    3.1,
    3,
    2.7,
    4.7,
    4.5,
    5,
    2.1,
    1.8,
    2.4,
    4.3
]

contInsuficiente = 0
contAceptable = 0
contSobresaliente = 0
sumaInsuficiente = 0
sumaAceptable = 0
sumaSobresaliente = 0
for grades in listOfGrades:
    if grades < 3:
        contInsuficiente = contInsuficiente  + 1
        sumaInsuficiente = sumaInsuficiente + grades
    elif grades >= 3 and grades < 4:
        contAceptable = contAceptable  + 1
        sumaAceptable = sumaAceptable + grades
    else:
        contSobresaliente = contSobresaliente  + 1
        sumaSobresaliente = sumaSobresaliente + grades

print("El promedio de los Insuficientes es ", sumaInsuficiente/contInsuficiente)
print("El promedio de los Aceptables es ", sumaAceptable/contAceptable)
print("El promedio de los Sobresaliente es ", sumaSobresaliente/contSobresaliente)