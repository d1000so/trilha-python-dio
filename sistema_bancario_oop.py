from time import sleep
from os import system


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


def exibir_menu():
    return f"""

        Escolha a opção:

        [1] Consultar Saldo
        [2] Extrato
        [3] Depositar
        [4] Sacar
        [5] Sair

        => """


    conta = Conta('123456-7', '1234', 0)
    tab = '\n' * 7

    class MenuBanco:
        def __init__(self, conta, agencia, saldo):
            self.conta = conta
            self.agencia = agencia
            self.saldo = saldo

    while True:
        opção = input(exibir_menu())
        if opção == '1':
            pass
        if opção == '2':
            pass
        if opção == '3':
            pass
        if opção == '4':
            pass
        if opção == '5':
            print(tab + '\tSaindo do programa. Até logo!' + tab)
            break
        else:
            print(tab + '\tOpção Inválida!' + tab)
            sleep(2)
            system('clear')
            

if __name__ == '__main__':

