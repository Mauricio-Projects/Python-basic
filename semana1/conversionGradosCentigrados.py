#paso1:  pedir los grados centigrados
valorCentigrados = int(input("Por Favor ingrese los grados centigrados: "))

#Paso2:  realizar la conversion con  la formula
valorFahrenheit= (valorCentigrados * 9/5)+32

#paso3: mostrar el resultado
print(f"el valor Fahrenheit es:  {valorFahrenheit}" ) 

## convertir de Fahrenheit a grados centigrados

#paso1:  pedir los grados
valorFahrenheit = int(input("Ingrese los grados Fahrenheit a convertir: "))

#Paso2:  realizar la conversion con  la formula
valorCentigrados= (valorFahrenheit - 32)/1.8

#paso3: mostrar el resultado
print(f"el valor Centigrados es:  {valorCentigrados}" ) 