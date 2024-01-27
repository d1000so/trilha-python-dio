import textwrap
from validarcpf import ValidarCPF


def menu():
    menu = """

        Escolha a opção:

        [d]\tDepositar
        [s]\tSacar
        [c]\tConsultar Extrato
        [u]\tCadastrar Cliente
        [l]\tListar Clientes
        [a]\tCadastrar Conta
        [q]\tSair

        => """
    return input(textwrap.dedent(menu))

        
def tratar_dados(string):
    # Dividir a string em partes usando vírgula como delimitador
    partes = string.split(',')

    # Aplicar strip() para remover espaços extras em cada parte
    partes_tratadas = [' '.join(palavra.strip() for palavra in parte.split()) for parte in partes]

    return partes_tratadas


def cadastrar_cliente(clientes):
    cliente = dict()
    cpf = input('\nDigite o CPF: ')
    # Validando CPF
    if not ValidarCPF.validar_cpf(cpf):
        print('\nATENÇÃO! CPF não é válido')
    else:
        # Verificando se o cliente já está cadastrado
        if any(cliente['cpf'] == cpf for cliente in clientes):
            print('\nATENÇÃO! Cliente já cadastrado!')
        else:
            # Recebendo dados de clientes
            cliente['cpf'] = cpf
            print('\nDigite o nome do cliente:', end=' ')
            nome = tratar_dados(input().upper())
            cliente['nome'] = nome[0]
            cliente['data_nascimento'] = input('Digite a data de nascimento (dd/mm/aaaa):')
            print('\nDigite Rua, num, bairro, cidade, UF (usar ","):', end=' ')
            endereco = tratar_dados(input().upper())
            cliente['endereco'] = f'{endereco[0]}, {endereco[1]} - {endereco[2]} - {endereco[3]}/{endereco[4]}'
            clientes.append(cliente)


def depositar(saldo, valor, extrato, /):

    if valor > 0:
        saldo += valor
        extrato += f'\nDeposito:  R$ {valor:>10.2f}'
        
    else:
        pass


def sacar():
    global extrato, saldo
    valor = float(input('\n    Digite o valor do saque: '))
    if limite_de_saque <= 0:
        print('\n    Limite de saque no dia excedido...')
    elif saldo < valor:
        print('\n    Saldo insuficiente...')
    elif valor > 0:
        saldo -= valor
        extrato += f'\nSaque:  R$ {valor:>10.2f}'
        limite_de_saque -= 1
        
    else:
        print('\nOPÇÃO INVÁLIDA!')


def exibir_extrato():
    if extrato == '':
        print('\n    Não foram realizadas operações...')
    else:
        extrato = '\n******* EXTRATO ********\n'
    print(extrato)
    print(f'\nSaldo:  R$ {saldo:>10.2f}')
    return saldo, extrato


def resposta_ao_cliente(resposta):
    if resposta == 'sucesso':
        print('\n    Operação realizada com sucesso...')
    elif resposta == 'erro':
        print('\n    Operação falhou!')
    elif resposta == 'opcao_invalida':
        print('\n    Opção inválida!')
    elif resposta == 'sair':
        print('\n    Obrigado por utilizar nossos...')


def main():
    LIMITE_DE_SAQUE = 3
    AGENCIA = '0001'

    saldo = 0
    limite = 500
    extrato = ''
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == 'd':
            valor = float(input('\n    Digite o valor do depósito: '))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == 's':
            pass

        elif opcao == 'c':
            pass

        elif opcao == 'c':
            pass

        elif opcao == 'l':
            pass

        elif opcao == 'a':
            pass

        elif opcao == 'q':
            pass
            break

        else:
            pass


if __name__ == '__main__':
    main()