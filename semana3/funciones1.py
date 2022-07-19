#imprimir la suma y la resta y la multiplicacion de 2 numeros.

#definir la funcion suma
def addTwoNumbers(n1,n2):
    suma = n1 + n2
    return suma

#definir la funcion resta
def subtrackTwoNumbers(n1,n2):
    suma = n1 - n2
    return suma

#definir la funcion multiplicacion
def multiplyTwoNumbers(n1,n2):
    suma = n1 * n2
    return suma


#funcion general para el calculo

def calculateResult(n1,n2,operation):
    
    if operation == "s":
        return addTwoNumbers(n1,n2)
    elif operation =="r":
        return  subtrackTwoNumbers(n1,n2)
    elif operation == "m":
        return  multiplyTwoNumbers(n1,n2)
    else:
        return  "error"
    


#solicito la informacion al usuario
number1 = int(input("Por favor ingrese el primer numero: "))
number2 = int(input("Por favor ingrese el segundo numero: "))

#llamado a la funcion
suma = calculateResult(number1,number2,"s")
resta = calculateResult(number1,number2,"r")
multiplicacion  = calculateResult(number1,number2,"m")

#imprimo los resultados
print(f"La suma es: {suma}")
print(f"La resta es: {resta}")
print(f"La multiplicacion es: {multiplicacion}")


