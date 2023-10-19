

# Sistema de pagamento de funcionários

from Sistema_Banco_digital.OperacoesBancarias import OperacoesUsuarios

def analisa_resposta(resposta=''):
    if resposta == 'não':
        return False
    elif resposta == 'sim':
        return True
    else:
        return True


# Interface do sistema para fucninários

loop = True

while loop:
    try:
        nome_funcionairo = str(input('informe o nome do funcionário? '))
    except:
        print('Nome inválido')
    else:
        funcionario = OperacoesUsuarios.Funcionarios(nome_funcionairo)

        pagamento = float(input('Informe o pagamento: '))

        funcionario.pagamento(pagamento)

        valor_pago = funcionario.consultar_saldo()[0]
        print(valor_pago)
    while loop:
        try:
            resp = str(input("Deseja fazer outra transação? [sim / não] ")).strip().lower()
        except:
            print('Resposta inválida!')
        else:
            loop = analisa_resposta(resp)
            if loop:
                break


print('>>>      Obrigado por usar nossos serviços! Volte sempre     <<<')