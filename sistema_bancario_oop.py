from datetime import datetime


class Conta:
    def __init__(self, numero, agencia, saldo):
        self.numero = numero
        self.agencia = agencia
        self._saldo = saldo


    @property
    def saldo(self):
        return self._saldo

    
    @saldo.setter
    def saldo(self, valor):
        if valor > 0:
            self._saldo = valor
        else:
            print('Conta não permite saldo negativo')


    def depositar(self, valor):
        self.valor = valor
        if valor > 0:
            self._saldo += valor
        else:
            print('Insira um valor positivo')


    def sacar(self, valor):
        self.valor = valor
        if valor > 0:
            self._saldo -= valor
        else:
            print('Insira um valor positivo')


conta = Conta('123456-7', '1234', 0)
conta.depositar(1500)
conta.sacar(500)

print(conta.saldo)

