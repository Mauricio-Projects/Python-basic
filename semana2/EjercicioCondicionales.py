#ejercicio con condicionales:  juego numero a encontrar

numeroAEncontrar = 7

numeroIngresadoPorElUsuario = int(input("Adivina cual es el número registrado en la variable: "))

if numeroIngresadoPorElUsuario > numeroAEncontrar:
    print("El número que estas buscando es menor al que ingresaste")
elif numeroIngresadoPorElUsuario < numeroAEncontrar:
    print("El número que estas buscando es mayor al numero ingresado")
#elif numeroIngresadoPorElUsuario == numeroAEncontrar:
else:
    print("Correcto!!! El numero que ingresaste es correcto.")

