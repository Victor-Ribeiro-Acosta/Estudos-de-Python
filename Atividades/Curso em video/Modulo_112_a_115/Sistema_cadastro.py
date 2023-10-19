
while True:
    print('=' * 20)
    print('\033[34mSISTEMA DE CADASTRO\033[m')
    print('=' * 20)
    print('''
0 - Analisar pessoas cadastradas
1 - Cadastrar nova pessoa
2 - Encerrar''')
    resp = int(input('Informe a ação desejada: '))
    if resp == 0:
        print('='*20)
        arquivo = open('nome.txt','r')
        print(f'{arquivo.read()}')
        arquivo.close()
        print('=' * 20)
    elif resp == 1:
        nome = str(input('Digite o nome: '))
        idade = int(input('Informe a idade: '))
        arquivo = open('nome.txt', 'r')
        registro = arquivo.readlines()
        registro.append(f'\n{nome:.<16}')
        registro.append(f'{idade}')
        arquivo = open('nome.txt', 'w')
        arquivo.writelines(registro)
        arquivo.close()
    else:
        break
print('\033[33m>> Programa encerrado! Volte sempre <<.\033[m')