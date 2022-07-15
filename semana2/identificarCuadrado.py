#pedirle al usuario el ancho y el alto de una figura geometrica y decirlke si es un rectangulo o un cuadrado

#se pide al usuario que ingrese el alto y el ancho
ancho = input("Por favor digite el ancho: ")
alto = input("Por favor digite el alto:")

#se crea la estructura del algoritmo
if ancho == alto:
    print("la figura es un cuadrado")
else:
    print("la figura es un rectangulo")
