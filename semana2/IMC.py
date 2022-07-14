#paso1: pedirle al usuario su peso.
peso = int(input("Por favor ingrese su peso en Kg: "))

#paso2:  pedirle al usuario su estatura
estatura = float(input("por favor ingrese su estatura en metros: "))


#paso3: Calcular el IMC
imc = peso / (estatura **2)

#paso4: Mostrar el IMC dependiendo del caso
if imc < 18.5:
    print("usted tiene una condicion de peso inferior al normal")
elif imc >= 18.5 and imc < 24.9:
    print("usted tiene una condicion de peso normal")
elif imc > = 25 and imc < 29.9:
    print("usted tiene una condicion de peso es superior al normal")
else:
    print("usted tiene sobrepeso")
print(f"su indice de masa corporal es de {imc} kg/m2")
