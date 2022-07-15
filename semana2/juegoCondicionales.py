
#ejercicio con condicionales:  juego numero a encontrar
numeroIngresadoPorElUsuario = 0
numeroAEncontrar = 7

    

while numeroIngresadoPorElUsuario != numeroAEncontrar:
    numeroIngresadoPorElUsuario = int(input("Adivina cual es el número registrado en la variable: "))

    if numeroIngresadoPorElUsuario > numeroAEncontrar:
        print("El número que estas buscando es menor al que ingresaste")
    elif numeroIngresadoPorElUsuario < numeroAEncontrar:
        print("El número que estas buscando es mayor al numero ingresado")
print("Correcto!!! El numero que ingresaste es correcto.")