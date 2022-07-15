#preguntar el total de una compra,  si el valor es mayor a 100.000, dar un descuento del 10%

#se pregunta al usuario el valor de la compra
valorCompra = int(input("Digite el valor de su Compra sin puntos: $"))

#se crea la logica del algoritmo

if valorCompra > 100000:
    valorDescuento = (valorCompra * 10) / 100 
    valorCompra = valorCompra - valorDescuento
    print(f"el valor de su compra con descuento es de ${valorCompra} pesos")
else:
    print(f"el valor de su compra es ${valorCompra} pesos")