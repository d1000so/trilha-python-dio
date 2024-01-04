import os

def pausa():
    input('''\n
    Enter para continuar...''')
    os.system('clear')


def mensage(resposta):
    if resposta == True:
        print('''\n
    Operação com sucesso...''')
    else:
        print('''\n
    Operação falhou!''')

menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] sair

"""

limite = 500
extrato = ''
saldo = 0
limite_de_saque = 36

while True:
    
    os.system('clear')
    print('Escolha a opção\n')

    opcao = input(menu)

    if opcao == 'd':

        os.system('clear')
        valor = float(input('Digite o valor do depósito: '))
        
        if valor > 0:
            saldo += valor
            extrato += f'\nR$ {valor:>10.2f} +'
            mensage(1)
        else:
            mensage(0)

        pausa()

    elif opcao == 's':

        os.system('clear')
        valor = float(input('Digite o valor do saque: '))

        if limite_de_saque <=0:
            print('\n    Limite de saque no dia excedido...')
            pausa()
        elif saldo < valor:
            print('\n    Saldo insuficiente...')
            pausa()
        elif valor > 500:
            print('\n    Limite de saque excedido...')
            pausa()
        elif valor > 0:
            saldo -= valor
            extrato += f'\nR$ {valor:>10.2f} -'
            limite_de_saque -= 1
            mensage(1)
            pausa()
        else:
            print('\n    Valor inválido...')
            pausa()

    elif opcao == 'e':
        os.system('clear')
        print('******* EXTRATO ********\n')
        print(extrato)
        print(f'\nR$ {saldo:>10.2f} S')
        pausa()

    elif opcao == 'q':
        os.system('clear')
        print('\n    Obrigado... Até Breve!\n\n\n')
        break

    else:
        print('\n    Opção inválida...')
        pausa()