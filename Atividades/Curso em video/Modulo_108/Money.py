# Funções Monetárias

def aumentar(valor, taxa):
    r = valor + (valor*taxa/100)
    return r

def subtrair(valor, taxa):
    r = valor - (valor*taxa/100)

def dobro(valor):
    r = valor*2
    return r

def dividir(valor):
    r = valor/2
    return r

def moeda(valor):
    return f'R$ {valor}'.replace('.', ',')