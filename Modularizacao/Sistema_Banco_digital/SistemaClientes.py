

from Sistema_Banco_digital.OperacoesBancarias import OperacoesUsuarios


conta_clientes = OperacoesUsuarios.ClientesBanco('Victor')

# Interface do SIstema para clientes

def atividades_clientes(operacao):
    if operacao == 1:

        valor = float(input('Informe o valor de saque: '))
        conta_clientes.saque(valor)
        print(conta_clientes.saldo)

    elif operacao == 2:

        valor = float(input('Informe o valor de depósito'))
        conta_clientes.deposito(valor)
        print(conta_clientes.saldo)

    elif operacao == 3:

        saldo_anterior = conta_clientes.consultar_saldo()[0]
        print(saldo_anterior)

    elif operacao == 4:

        conta_clientes.consultar_historico()

    elif operacao == 5:
        return True

    else:
        print('Operação Inválida')
        return False


while True:

    print('''
    1 - Saque
    2 - Depositar
    3 - Consultar Saldo
    4 - Consultar Histórico
    5 - finalizar
    ''')
    try:

        operacao = int(input('Qual operação você desea fazer? '))

    except ValueError:

        print('Informe um valor de acordo com o menu!')

    else:

        print()
        if atividades_clientes(operacao):
            break
        print()
        print('='*50)

print('>>> Operação finalizada! Obrigado por usar nossos serviços. <<<')


