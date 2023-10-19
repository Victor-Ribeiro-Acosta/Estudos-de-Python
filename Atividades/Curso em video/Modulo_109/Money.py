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
    return f'R$ {valor}'.replace('.', ',')
