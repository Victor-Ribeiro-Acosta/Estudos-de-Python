

from datetime import date
import os


# Lógica de operações básicas

class OperacoesBanco():

    def __init__(self, nome):
        self.nome = nome
        self.arquivo = 'C:/Users/Thiago/Documents/Victor/Python/Projetos Python/Sistema_Banco_digital/Extratos/Extrato_' + self.nome + '.txt'
        self.criar_extrato()
        self.saldo = self.consultar_saldo()[1]


    def criar_extrato(self):

        if not os.path.exists(self.arquivo):
            with open(self.arquivo, 'wt+', encoding='UTF-8') as txt:
                extrato = txt.write('Movimentações na Conta\nNome: ' + self.nome+'\n\n')


    def consultar_saldo(self):

        with open(self.arquivo) as txt:
            retorno = txt.readlines()
            ultimo_saldo = retorno[len(retorno) - 2]
            try:
                saldo_inicial = float(ultimo_saldo.split(':')[1])

            except ValueError:
                return ['Saldo disponivel: 0',0]
            else:
                return [ultimo_saldo, saldo_inicial]


    def consultar_historico(self):

        with open(self.arquivo) as txt:
            linhas = txt.readlines()
            for linha in linhas:
                print(linha.split('\n')[0])



# Logica para clientes
class ClientesBanco(OperacoesBanco):

    def __init__(self, nome):

        super().__init__(nome)
        self.tipo_transacao = ''

    def deposito(self, valor=0):

        if valor < 10000:
            self.saldo += valor
            self.tipo_transacao = 'Depósito'
            self.extrato(str(valor))
            print('Operação realizada com sucesso!')
        else:
            print('Esse valor excede o limite para depósitos')

    def saque(self, valor=0):

        if self.saldo >= valor:
            self.saldo -= valor
            self.tipo_transacao = 'Saque'
            self.extrato(str(valor))
            print('Operação realizada com sucesso!')
        else:
            print('Saldo insuficiente!')


    def extrato(self, valor):

        data = date.today()
        with open(self.arquivo, 'a') as txt:
            txt.write('\n\nData da Transação: ' + str(data)+'\n')
            txt.write('Tipo de Transação: '+ self.tipo_transacao+'\n')
            txt.write('Valor: ' + valor+'\n')
            txt.write('='*35)
            txt.write('\nValor disponível: ' + str(self.saldo)+'\n')
            txt.write('=' * 35)



# Logica para funcionários cadastrados

class Funcionarios(OperacoesBanco):

    def __init__(self,nome):

        super().__init__(nome)

    def pagamento(self, valor=0):

        self.valor = valor
        self.inss = self.valor * 0.1
        taxa = 10

        if valor < 10000:
            self.valor -= (taxa + self.inss)
            self.saldo += self.valor
            self.extrato(str(valor))
            print('Pagamento realizado com sucesso!')
        else:
            print('Esse valor excede o limite para depósitos')


    def extrato(self, valor):

        data = date.today()
        with open(self.arquivo, 'a') as txt:
            txt.write('\n\nData da Transação: ' + str(data)+'\n')
            txt.write('Valor depositado: ' + valor+'\n')
            txt.write('Desconto INSS: '+str(self.inss) + '\n')
            txt.write('Taxa de Conta: 10' + '\n')
            txt.write('Total: ' + str(self.valor) + '\n')
            txt.write('='*35)
            txt.write('\nTotal na conta: ' + str(self.saldo)+'\n')
            txt.write('=' * 35)

