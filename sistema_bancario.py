import os

menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] sair

"""

limite = 500
extrato = ''
saldo = 0
numero_saques = 0
LIMITE_SAQUE = 3

while True:
    
    os.system('clear')
    print('Escolha a opção\n')

    opcao = input(menu)

    if opcao == 'd':

        os.system('clear')
        valor = float(input('Digite o valor do depósito: '))
        
        if valor > 0:
            saldo += valor
            extrato += f'\nDeposito: R$ {valor:>10.2f}'
            print('\nOperação realizada com sucesso...')
        else:
            print('\nOperação falhou!\n')

        input('\nPrecione Enter para continuar...')
        os.system('clear')

    elif opcao == 's':

        os.system('clear')
        valor = float(input('Digite o valor do saque: '))

        if numero_saques >= LIMITE_SAQUE:
            print('\nLimite de saque no dia excedido...\n')
            input('\nPrecione Enter para continuar...')
            os.system('clear')
        elif saldo < valor:
            print('\nSaldo insuficiente...\n')
            input('\nPrecione Enter para continuar...')
            os.system('clear')
        elif valor > 500:
            print('\nLimite de saque excedido...\n')
            input('\nPrecione Enter para continuar...')
            os.system('clear')
        elif valor > 0:
            saldo -= valor
            extrato += f'\nSaque:    R$ {valor:>10.2f}'
            numero_saques += 1
            print('\nOperação realizada com sucesso...\n')
            input('\nPrecione Enter para continuar...')
            os.system('clear')
        else:
            print('\nValor inválido...\n')
            input('\nPrecione Enter para continuar...')
            os.system('clear')

    elif opcao == 'e':
        os.system('clear')
        print('******* EXTRATO ********')
        if extrato == '':
            print('\nNão foram realizadas movimentações.\n')
        else:
            print(extrato)
            print(f'\nSaldo:    R$ {saldo:>10.2f}')
        input('\nPrecione Enter para continuar...')
        os.system('clear')

    elif opcao == 'q':
        os.system('clear')
        print('\nObrigado... Até Breve!\n\n\n')
        break

    else:
        print('\nOpção inválida...\n')
        input('\nPrecione Enter para continuar...')
        os.system('clear')