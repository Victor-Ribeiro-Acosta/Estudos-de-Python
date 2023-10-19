# Inserir dados monetários

import Money
cash = float(input('Informe o valor: '))
print(f'Aumentado 10%, o novo valor é {Money.aumentar(cash, 10, format = True)}')
print(f'A metade desse valor é {Money.dividir(cash, format = True)}')
print(f'O dobro desse valor é {Money.dobro(cash, format = True)}')
