# simular un inicio de sesion con una contraseñaguardada.



maxRetries = 3
storedPassword = "ab123"
usserPassword = input("Digite su contraseña: ")


cont = 0

while storedPassword != usserPassword and cont < maxRetries:   
    print("la contraseña no coincide")
    cont += 1 
    print("Valor del contador ", cont)
    usserPassword = input("Por favor ingresa nuevamente la contraseña: ")

if cont >= maxRetries:
    print("Te equivocaste mas de tres veces.  Te hemos bloqueado.")
else:    
    print("Contraseña Correcta!!.  Puede iniciar sesion")