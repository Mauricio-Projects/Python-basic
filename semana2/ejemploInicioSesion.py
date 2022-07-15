# simular un inicio de sesion con una contraseaguardada en Db.


storedPassword = "ab123"
newPassword = input("Digite su contrasenia: ")

while storedPassword != newPassword:    
    
    newPassword = input("la contrasena no coincide.  Digite su contrasenia nuevamente: ")
    
print("Contrasenia Correcta!!.  Puede iniciar sesion")