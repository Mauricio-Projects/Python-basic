#pedirle al usuario dos valores numericos. imprimir el mayor de ellos.


#se solicitan al usuario los dos numeros
valor1 = int(input("Ingrese el primer numero: "))
valor2 = int(input("Ingrese el segundo numero: "))

#se crea la logica del programa y se imprime en pantalla.
if valor1 > valor2:
    print(f"el número con mayor valor es : {valor1}, que es el primer numero ingresado")
if valor1 == valor2:
    print("los numeros ingresados son iguales en su valor")
else:
    print(f"el segundo numero ingresado es el de mayor valor: {valor2}")
