# Inserir dados monetários

import Money
cash = float(input('Informe o valor: '))
print(f'Aumentado 10%, o novo valor é {Money.aumentar(cash, 10)}')
print(f'A metade desse valor é {Money.dividir(cash)}')
print(f'O dobro desse valor é {Money.dobro(cash)}')
