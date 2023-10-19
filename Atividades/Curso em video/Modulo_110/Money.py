# Funções Monetárias

def aumentar(valor, taxa, format = False):
    r = valor + (valor*taxa/100)
    if format == True:
        r = moeda(r)
    return r

def subtrair(valor, taxa, format = False):
    r = valor - (valor*taxa/100)
    if format == True:
        r = moeda(r)
    return r

def dobro(valor, format = False):
    r = valor*2
    if format == True:
        r = moeda(r)
    return r

def dividir(valor, format = False):
    r = valor/2
    if format == True:
        r = moeda(r)
    return r

def moeda(valor):
    return f'R$ {valor:.2f}'.replace('.', ',')

def info(dado, N_format = False):
    print(f'Aumentado 10%, esse valor passa a ser {aumentar(dado,10, format = N_format)}')
    print(f'Reduzindo 10%, esse valor passa a ser {subtrair(dado,10, format = N_format)}')
    print(f'A metade desse valor é {dividir(dado, format = N_format)}')
    print(f'O dobro desse valor é {dobro(dado, format = N_format)}')