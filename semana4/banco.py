import random
#hacer una clase que se llame CuentaBancaria.
#artibutos: 
# numero de la cuenta -> es aleatorio entre 1.000 y 10.000
# saldo
# métodos:
# retirar
# depositar
#ejercicio: agregar condición que saque error si el saldo es negativo
#ejercicio: cobrar una comisión del 4 pesos por cada 1000 cuando el monto de la consignación sea mayor a 10.000
#ejercicio opcional: crear una lista de cuentas y agregar la posibilidad de crear una cuenta nueva o eliminar una cuenta
    #cuando se vaya a retitar o a consignar, se debe ingresar el número de la cuenta
# ejercicio opcional: crear una clase persona y a la clase cuenta agregarle una persona pidiéndole su cédula. 
#Hay que construir una lista de personas. Si la persona no existe, se debe crear.
class CuentaBancaria:
    def __init__(self,saldoInicial):
        self.numeroCuenta = random.randint(1000,10000)
        self.saldo = saldoInicial

    def retirar(self, monto):
        if monto > self.saldo:
            print("Fondos insuficientes")
        else:
            self.saldo = self.saldo - monto
            print("Retiro Exitoso")

    def consignar(self,monto):
        if monto > 10000:
            comision = monto * 4 /1000
            monto = monto - comision
            print("La comisión por la consignación es de : ", comision)
            self.saldo = self.saldo + monto
        else:
            self.saldo = self.saldo + monto


    def consultarSaldo(self):
        print("________________")
        print("Cuenta: ",self.numeroCuenta)
        print("Saldo: ",self.saldo)
        print("________________")

def buscarCuentas(mensajeOperacion):
    #pedir numero de cuenta del usuario
        numCuenta = int(input(mensajeOperacion))
        #buscar la cuenta del usuario.  Cuando se encuentre, imprimir el saldo.
        for cuenta in listaDeCuentas:
            if cuenta.numeroCuenta == numCuenta:
                return [True, cuenta]
        return False
listaDeCuentas = []

while True:
    operacion = input("Ingrese N para crear una nueva cuenta, S para consultar el saldo, R para retirar y C para consignar: ").upper()
    if operacion == "N":
        saldoInicial = float(input("Bienvenido al banco XYZ. Para crear su cuenta bancaria, ingrese el saldo inicial de la cuenta: "))
        cuenta = CuentaBancaria(saldoInicial)
        listaDeCuentas.append(cuenta)
        print("Cuenta creada con exito.  el numero de la cuenta es: ", cuenta.numeroCuenta)
        
    elif operacion == "S":
        resultadoLista = buscarCuentas("Por favor ingrese el numero de cuenta que quiere consultar: ")
        if resultadoLista[0]:
            cuenta = resultadoLista[1]
            cuenta.consultarSaldo()

    elif operacion == "R":
        resultadoLista = buscarCuentas("Por favor ingrese el numero de cuenta que quiere retirar: ")
        if resultadoLista[0]:
            monto = float(input("Ingrese el monto a retirar: "))
            cuenta = resultadoLista[1]
            cuenta.retirar(monto)
    elif operacion == "C":
        resultadoLista = buscarCuentas("Por favor ingrese el numero de cuenta que quiere consignar: ")
        if resultadoLista[0]:
            monto = float(input("Ingrese el monto a consignar: "))
            cuenta = resultadoLista[1]
            cuenta.consignar(monto)
    else:
        print("Operación incorrecta")

    print(listaDeCuentas)