def LeiaInt(m):
    while True:
        try:
            num = int(input(m))
        except():
            print('Erro, o valor digitado não é um número válido')
        except(KeyboardInterrupt):
            print('O usuário encerrou o programa sem completar o processo')
            return 0
        else:
            return f'{num}'
            break

def LeiaFloat(m):
    while True:
        try:
            num = float(input(m))
        except:
            print('Número inválido! Informe um valor seguindo essa formatação [00.000].')
        else:
           return f'{num:.2f}'.replace('.', ',')


int = LeiaInt('Informe um número INTEIRO: ')
flt = LeiaFloat('Informe um número REAL: ')
print(int)
print(flt)