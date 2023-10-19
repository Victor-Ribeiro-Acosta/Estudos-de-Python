# Inserir dados monetários

import Money
cash = float(input('Informe o valor: '))
print(f'Aumentado 10%, o novo valor é {Money.moeda(Money.aumentar(cash, 10))}')
print(f'A metade desse valor é {Money.moeda(Money.dividir(cash))}')
print(f'O dobro desse valor é {Money.moeda(Money.dobro(cash))}')
