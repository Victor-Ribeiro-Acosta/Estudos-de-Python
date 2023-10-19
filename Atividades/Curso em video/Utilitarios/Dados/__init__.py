def LeiaDinheiro(msg):
    validar = False
    while validar == False:
        n = str(input(msg)).replace(',', '.').strip()
        if n.isalpha() or n == '':
            print(f'ATENÇÃO! {n} não é um número válido')
        else:
            validar == True
            return float(n)
