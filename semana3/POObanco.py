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
    
    def withdraw(self, acount):
        
        if self.balance < acount:
            print("Insufficient Founds")
        else:
            self.balance = self.balance - acount
            print("--Successful Withdrawal--")

        
    def record(self, acount):
        if acount > 10000:
            commission = acount * 4 / 1000
            print("The commission of the consignment of: ", commission)
            acount = acount - commission
            self.balance = self.balance + acount
        else:
            self.balance = self.balance + acount

    def checkBalance(self):
        print("Account: ", self.accountNumber)
        print("Balance: ", self.balance)
        print("------------------")

# cuenta1 = CuentaBancaria(10000)
# cuenta1.checkBalance()
# cuenta1.retirar(500)
# cuenta1.consignar(20000)


listOfAccount = []
while True:
    operacion = input("Enter to new account 'N', Enter 'S' to check balance, 'R' to withdraw and 'C' to consing: ")
    
    if operacion == "N":
        initialBalance = float(input("Welcome to the Bank AMG.\nTo create a bank account enter the opening balance: "))
        account = BankAccount(initialBalance)
        listOfAccount.append(account)
        print("Account created successfully. The account number is: ", account.accountNumber )

    elif operacion == "S":
        #pedir el numero de cuenta al usuario
        numAccount = int(input("Please, enter your number account: "))
        #buscar la cuenta del usuario. cuando se encuentre imprimir el saldo
        for account in listOfAccount:
            if account.accountNumber == numAccount:
                print("Account found")
                account.checkBalance()
        
    elif operacion == "R":
        amount = float(input("Enter the value you want to withdraw: "))
        listOfAccount.withdraw(amount)
        
    elif operacion == "C":
        amount = float(input("Enter the value you want to record: "))
        listOfAccount.record(amount)
        print("--Successful consignment--")
