#Paso1: pedir total de la factura
totalFactura = int(input("Ingrese el valor de la factura: $"))

#Paso2: Pedir porcentaje de la propina que se quiere dar
porcentajePropina = int(input("Ingrese el porcentaje de la propina: %"))

#Paso3: calcular valor del IVA 19%
valorIva= totalFactura * 0.19

#Paso4:calcular subtotal 
subtotalFactura= totalFactura-valorIva

#Paso5: Calcular valor de la propina
propina= subtotalFactura * porcentajePropina / 100

#paso6: Mostrar resultado. 
print(f"el valor del Iva es : ${valorIva} la propina es de ${propina} pesos")