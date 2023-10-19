
from Sistema import Interface

def AnalisarArquivo(nome):
    #     Analisa se o arquivo de texto .TXT existe no projeto ou não
    try:
        arq = open(nome, 'rt')
    except FileNotFoundError:
        print('Arquivo não encontrado')
        return False
    else:
        return True


def ListarArquivo(nome):
  # Mostra os dados de maneira mais visual
    try:
        arq = open(nome, 'rt')
    except:
        print('Erro ao mostrar o arquivo')
    else:
        for l in arq:
            print(f'{l:<}')
            #linha = l.split(';')       quebrar dados da linha em dois
                                        #mostrar cada um em separado na lista
        arq.close()
    Interface.lin()


def CriarArquivo(nome):

    # Cria um arquivo de texto para receber os dados

    try:
        arq = open(nome, 'wt+')     # wt = abrir modo de escrita; + = em caso de não existir o arquivo, cria-lo
        arq.close
    except:
        print('Não foi possivel criar o arquivo!')
    else:
        arq = open(nome, 'at')
        n = 'Nome'
        arq.write(f'{n:<20}Idade\n')
        print('Aquivo criado com sucesso!')
        arq.close()


def EditarArquivo(arquivo, nome, idade):
    try:
        arq = open(arquivo, 'at')       # at = modo apendice (permite inserir dados)
    except:
        print('Falha ao salvar registro!')
    else:
        arq.write(f'{nome:.<20}{idade} anos\n',)         # escrever dados no arquivo
        arq.close()
        print(f'Registro de {nome} salvo com sucesso!')

