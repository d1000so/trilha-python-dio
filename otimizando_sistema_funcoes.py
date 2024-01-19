import os
from validarcpf import ValidarCPF


def tratar_dados(string):
    # Dividir a string em partes usando vírgula como delimitador
    partes = string.split(',')

    # Aplicar strip() para remover espaços extras em cada parte
    partes_tratadas = [' '.join(palavra.strip() for palavra in parte.split()) for parte in partes]

    return partes_tratadas


def cadastrar_cliente():
    cliente = dict()
    cpf = input('Digite o CPF: ')
    # Validando CPF
    if not ValidarCPF.validar_cpf(cpf):
        print('CPF não é válido')
    else:
        if cpf in clientes:
            print('Cliente já cadastrado!')
        else:
            # Recebendo dados de clientes
            cliente['cpf'] = cpf
            print('Digite o nome do cliente:', end=' ')
            nome = tratar_dados(input().upper())
            cliente['nome'] = nome[0]
            cliente['data_nascimento'] = input('Digite a data de nascimento (dd/mm/aaaa):')
            print('Digite Rua, num, bairro, cidade, UF (usar ","):', end=' ')
            endereco = tratar_dados(input().upper())
            cliente['endereco'] = f'{endereco[0]}, {endereco[1]} - {endereco[2]} - {endereco[3]}/{endereco[4]}'
            clientes.append(cliente)
            del cliente


def depositar(saldo, consulta):
    limpar_tela()
    valor = float(input('\n    Digite o valor do depósito: '))

    if valor > 0:
        saldo += valor
        consulta += f'\nR$ {valor:>10.2f} +'
        mensagem('sucesso')
    else:
        mensagem('erro')

    return saldo, consulta


def sacar(saldo, consulta, limite_de_saque):
    limpar_tela()
    valor = float(input('\n    Digite o valor do saque: '))

    if limite_de_saque <= 0:
        mensagem('limite_saque_dia')
        print('\n    Limite de saque no dia excedido...')
    elif saldo < valor:
        print('\n    Saldo insuficiente...')
    elif valor > 0:
        saldo -= valor
        consulta += f'\nR$ {valor:>10.2f} -'
        limite_de_saque -= 1
        mensagem('sucesso')
    else:
        mensagem('opcao_invalida')

    return saldo, consulta, limite_de_saque


def consultar(saldo, consulta):
    limpar_tela()
    print(consulta)
    print(f'\nR$ {saldo:>10.2f} +')
    pausar()


def mensagem(resposta):
    limpar_tela()
    if resposta == 'sucesso':
        print('\n    Operação com sucesso...')
    elif resposta == 'erro':
        print('\n    Operação falhou!')
    elif resposta == 'opcao_invalida':
        print('\n    Opção inválida!')
    elif resposta == 'limite_saque_dia':
        print('\n    Limite de saque no dia excedido...')
    elif resposta == 'sair':
        print('\n    Obrigado por utilizar nossos...')
    pausar()


def limpar_tela():
    os.system('clear')  # Substitua por métodos mais portáteis para limpar a tela


def pausar():
    input('''\n\n
    Precione enter para continuar...''')
    limpar_tela()


if __name__ == '__main__':
    clientes = []
    limite_de_saque = 3
    limite = 500
    consulta = '******* EXTRATO ********\n'
    saldo = 0

    while True:
        menu = """

        Escolha a opção:

        [cc] Cadastrar Cliente
        [c] Consultar Extrato
        [d] Depositar
        [s] Sacar
        [lc] Listar Clientes
        [q] Sair

        => """

        opcao = input(menu)

        if opcao == 'cc':
            cadastrar_cliente()
        elif opcao == 'd':
            saldo, consulta = depositar(saldo, consulta)
        elif opcao == 's':
            saldo, consulta, limite_de_saque = sacar(saldo, consulta, limite_de_saque)
        elif opcao == 'c':
            consultar(saldo, consulta)
        elif opcao == 'q':
            mensagem('sair')
            break
        elif opcao == 'lc':
            print(clientes)
        else:
            mensagem('opcao_invalida')




