
from Sistemas.Registros_login import registros
import csv
import os

# Lógica do sistema de registro de funcionários
class RegistroFuncionarios():

    def __init__(self):
        # métodod construtor

        self.cabeçalhos = ['Nome', 'Setor', 'Cargo', 'Data de Contratação', 'Salário', 'Situação']
        self.dados = []
        self.funcionario = ''

    def gravar_registros(self):

        # Registrar informações de funcionários no banco de dados
        for cab in self.cabeçalhos:
            info = str(input(f'Informe {cab}: '))
            self.dados.append(info)

        self.inserir_dados()

    def criar_banco_dados_func(self, pasta_dest, nome):

        # Criar banco de dados
        self.caminho2 = registros.usuario().caminho
        self.diretorio2 = self.caminho2 + pasta_dest +'/'+ nome + '.csv'
        if not os.path.exists(self.diretorio2):
            with open(self.diretorio2, 'w+') as arq:
                arquivo = csv.writer(arq)
                arquivo.writerow(self.cabeçalhos)

    def inserir_dados(self):

        with open(self.diretorio2, 'a', newline='') as arquivo:
            registro = csv.writer(arquivo, delimiter=',')
            registro.writerow(self.dados)

    def mostrar_dados(self,nome=''):

        with open(self.diretorio2, 'r', newline='') as arquivo:
            funcionarios = csv.reader(arquivo, delimiter=',')
            for funcionario in funcionarios:
                if funcionario[0].lower() == nome.lower():
                    self.funcionario = funcionario
                    return True
        return False

    def encerrar_processo(self, resp='não'):
        # Encerrar operação no sistema
        if resp == 'sim':
            return True
        return False
