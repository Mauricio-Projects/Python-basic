#Paso 1 : pedirle al usuario el total de la factura
totalFactura = int(input("Por favor ingrese el total de la factura: $"))

#Paso 2: Pedirle al usuario el valo que quiere dar de propina:
valorPropina = int(input("Por favor ingrese el porcentaje de la propina: %"))

#hacer el calculo de la propina
propina =  totalFactura * valorPropina / 100

#Mostrarle al usuario el valor de la propina
print(f"El valor de la propina es ${propina} pesos.")

