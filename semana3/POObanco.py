#hacer una clase que se llame cuenta bancaria
#atributos:  #numero de cuenta (aleatorio),  saldo,
#metodos: retirar, depositar

#ejercicio: agregar condicion si el saldo es negativo
#ejercicio:  cobrar una comision del 4 por 1000 cuando el momento de la consignacion sea mayor a 10.000
#ejercicio opcional:  crear una lista de cuentas y agregar la posibilidad de crear una cuenta nueva o eliminarla.
                    #cuando se vaya a retirar o consignar se debe ingresar el numero de la cuenta.

import random

class BankAccount:
    def __init__(self, initialBalance):
        self.accountNumber = random.randint(1000,10000) 
        self.balance = initialBalance
    
    def withdraw(self, amount):
        
        if self.balance < amount:
            print("Insufficient Founds")
        else:
            self.balance = self.balance - amount
            print("--Successful Withdrawal--")

        
    def record(self, amount):
        if amount > 10000:
            commission = amount * 4 / 1000
            print("The commission of the consignment of: ", commission)
            amount = amount - commission
            self.balance = self.balance + amount
        else:
            self.balance = self.balance + amount

    def checkBalance(self):
        print("Account: ", self.accountNumber)
        print("Balance: ", self.balance)
        print("------------------")

# cuenta1 = CuentaBancaria(10000)
# cuenta1.checkBalance()
# cuenta1.retirar(500)
# cuenta1.consignar(20000)


initialBalance = float(input("Welcome to the Bank AMG.\nTo create a banl account enter the opening balance: "))
savingAcoount = BankAccount(initialBalance)
while True:
    operacion = input("Enter 'S' to check balance, 'R' to withdraw and 'C' to consing: ")
    if operacion == "S":
        savingAcoount.checkBalance()

    elif operacion == "R":
        amount = float(input("Enter the value you want to withdraw: "))
        savingAcoount.withdraw(amount)
        
    elif operacion == "C":
        amount = float(input("Enter the value you want to record: "))
        savingAcoount.record(amount)
        print("--Successful consignment--")
