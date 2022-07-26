#hacer una clase que se llame cuenta bancaria
#atributos:  #numero de cuenta (aleatorio),  saldo,
#metodos: retirar, depositar
import random

class CuentaBancaria:
    def __init__(self, saldoInicial):
        self.numero = random.randint(1000,10000) 
        self.saldo = saldoInicial
    
    def retirar(self, monto):
        self.saldo = self.saldo - monto
        
    def consignar(self, monto):
        self.saldo = self.saldo + monto

    def consultarSaldo(self):
        print("Cuenta: ", self.numero)
        print("Saldo: ", self.saldo)
        print("------------------")

cuenta1 = CuentaBancaria(10000)
cuenta1.consultarSaldo()
cuenta1.retirar(500)
cuenta1.consignar(20000)


