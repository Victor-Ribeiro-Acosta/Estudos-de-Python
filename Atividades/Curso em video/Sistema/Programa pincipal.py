from Sistema.Interface import*
from Sistema.Arquivos import*

    # Programa Principal
arquivo = 'Lista de Cadastros.txt'
if not AnalisarArquivo(arquivo):
    CriarArquivo(arquivo)

titulo('Sistema de Cadastro')

while True:
    menu(['Listar cadastros', 'Cadastrar nova pessoa', 'Sair'])
    try:
        o = int(input('Escolha uma Opção: '))
    except:
        print('ERRO! Escolha uma opção válida.')
    else:
        if o == 1:
            Interface.titulo('Listar cadastros')
            ListarArquivo(arquivo)
        elif o == 2:
            titulo('Cadastrar nova pessoa')
            nome = str(input('Digite o nome: '))
            idade = int(input('Informe a idade: '))
            EditarArquivo(arquivo, nome, idade)
        elif o == 3:
            titulo('Saindo do sistema')
            break
        else:
            print('ERRO! Escolha uma opção válida')