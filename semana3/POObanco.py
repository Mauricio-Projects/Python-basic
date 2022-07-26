#hacer una clase que se llame cuenta bancaria
#atributos:  #numero de cuenta (aleatorio),  saldo,
#metodos: retirar, depositar

#ejercicio: agregar condicion si el saldo es negativo
#ejercicio:  cobrar una comision del 4 por 1000 cuando el moento de la consignacion sea mayo a 10000
import random

class BankAccount:
    def __init__(self, initialBalance):
        self.accountNumber = random.randint(1000,10000) 
        self.balance = initialBalance
    
    def withdraw(self, monto):
        
        if self.balance < amount:
            print("Fondos Insuficientes")
        else:
            self.balance = self.balance - monto
            print("--Successful Withdrawal--")

        
    def record(self, monto):
        self.balance = self.balance + monto

    def checkBalance(self):
        print("Cuenta: ", self.accountNumber)
        print("Saldo: ", self.balance)
        print("------------------")

# cuenta1 = CuentaBancaria(10000)
# cuenta1.checkBalance()
# cuenta1.retirar(500)
# cuenta1.consignar(20000)


initialBalance = float(input("Bienvenido al Banco AMG.\nPara crear su cuenta bancaria, ingrese el saldo inicial: "))
savingAcoount = BankAccount(initialBalance)
while True:
    operacion = input("Ingrese 'S' para consultar el saldo, 'R' para retirar y 'C' para consignar: ")
    if operacion == "S":
        savingAcoount.checkBalance()

    elif operacion == "R":
        amount = float(input("Ingrese el monto que quiere Retirar: "))
        savingAcoount.withdraw(amount)
        
    elif operacion == "C":
        amount = float(input("Ingrese el monto que quiere Consignar: "))
        savingAcoount.record(amount)
        print("--Successful consignment--")
