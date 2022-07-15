#Precio de base los huevos = 1800
#Precio de base las arepas = 5000

#si alguien compra mas de 10 canastas, y ademas compra 10 pqt de arepas el precio es 800
#si alguien compra mas de 10 canastas de huevos y ademas compra 10 paquetes de arepas.
# el precio de los huevos es de 1000 y el de las arepas 2000

#Paso1: preguntar cuantos huevos quiere comprar la persona
cantidadHuevos = int(input("Digite la cantidad de cajas de huevos que quiere comprar: "))

#paso2: preguntar si la persona quiere comprar arepas
quiereArepas = input("Usted quiere llevar Arepas? ")

#paso3:  preguntar si la persona quiere comprar arepas?
cantidadArepas = 0
if quiereArepas == "si" or "SI" or "Si":
    cantidadArepas = int(input("Digite la cantidad de paquetes de arepas que quiere comprar: "))


#paso4: calcular el total de compra
precioHuevos = 1800
precioArepas = 5000

if cantidadHuevos > 10:
    precioHuevos = 1000

if cantidadArepas > 10 and cantidadHuevos > 10:
    precioHuevos = 800
    precioArepas = 2000

#se realizar la operacion
totalCompra = precioHuevos * cantidadHuevos + precioArepas * cantidadArepas

print(f"El total de su compra es de {totalCompra} pesos.")