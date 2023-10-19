
import csv
import os


class usuario():

    def __init__(self):

        self.caminho = 'C:/Users/Thiago/Documents/Victor/Python/Projetos Python/Sistemas/'


    def criar_banco_dados_us(self,pasta_dest, nome):

        self.diretorio = self.caminho + pasta_dest +'/'+ nome + '.csv'
        if not os.path.exists(self.diretorio):
            with open(self.diretorio, 'w+') as arq:
                arquivo = csv.writer(arq)
                arquivo.writerow(('Usuario', 'Data de Nascimento', 'CPF', 'Email', 'Senha'))


    def registrar_usuario(self, usuario, data_nasc, cpf, email, senha):

        with open(self.diretorio, 'a', newline='') as arq:
            arquivo = csv.writer(arq, delimiter=' ')
            arquivo.writerow([usuario, data_nasc, cpf, email, senha])
        print('Novo usuário registrado com sucesso!')


    def logar(self, usuario, senha):

        with open(self.diretorio, 'r') as arq:
            registros = csv.reader(arq, delimiter=',')
            for lin in registros:
                if lin[0].lower() == usuario.lower() and lin[4] == senha:
                    return True

            return False
