#ejercicio4 : realizar un sistema de calificaciones
#pedir la calificacion de un examen de un usuario (0-5)
#0 -3 insuficiente (3 no incluido)
#3 - 4 acaptable (4 no incluido)
#4 - 4.6 imprimir sobresaliente (4.6 no incluido)
#4.6 - 5 imprimir excelente
#en cualquier otro rango imprimir calificacion errada

#se solicita al usuario ingrese el valor de la calificacion
calificacion = float(input("Por favor ingrese la calificacion: "))

#se realiza logica del algoritmo
if calificacion >=0 and calificacion <= 3.0:
    print("su calificacion es insuficiente")
elif calificacion >= 3.1 and calificacion <= 3.9:
     print("su calificacion es aceptable")
elif calificacion >= 4 and calificacion <= 4.5:
     print("su calificacion es sobresaliente")
elif calificacion >= 4.6 and calificacion <= 5:
    print("su calificacion es Excelente") 
else:
     print("usted digito un número erroneo")