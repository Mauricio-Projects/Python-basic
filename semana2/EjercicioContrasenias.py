#se solicitan dos contraseñas, se evaluan si son diferentes y dependiendo de eso se retipe el while.
contraseniasIguales = False

while contraseniasIguales == False:
    contrasenia1 = input("ingrese contraseña # 1: ")
    contrasenia2 = input("ingrese contraseña # 2: ")
    if contrasenia1 == contrasenia2:
        contraseniasIguales = True
    else:
        print("Las contraseas son diferentes.  Por favor ingreselas nuevamente.")
print("las contrasenias coinciden.")
