
# Jogo da velha

def validar(l, n, j):
    # Função para validar as informações das jogadas
    if 0 <= l <= 2 and 0 <= n <= 2:
        if j == 'x' or j == 'o':
            return True
        else:
            return False
    else:
        return False


def avalia_resultado(tab):
    # Função para analisar o resultado

    for t in tab: # Avaliando se alguma das linhas foi completada
        if t.count('x') == 3:
            print('X venceu!')
            return True
            break

        if t.count('o') == 3:
            print('O venceu!')
            return True
            break

    for i in range(3):  # Avaliando se alguma coluna foi completada
        if tab[0][i] == tab[1][i] == tab[2][i]: # Avalaiando se todas as posições da coluna possuem mesmo valor e se esse é diferente de 0
            if tab[0][i] == 'x':
                print('X venceu!')
                return True
                break

            if tab[0][i] == 'o':
                print('O venceu!')
                return True
                break

    if tab[0][0] == tab[1][1] == tab[2][2] != 0 or tab[0][2] == tab[1][1] == tab[2][0] != 0:    #Avaliando se as diagonais possuem mesmo valor e se esse é diferente de 0

        if tab[1][1] == 'x':
            print('X venceu')
            return True

        if tab[1][1] == 'o':
            print('O venceu')
            return True
    return False


# Iniciando Jogo

tab = [[0,0,0],[0,0,0],[0,0,0]]

while True:

    fim = 0
    for t in tab:
        print(t)
        if 0 in t:      # Analisando se ainda existem possibildades para jogo
            fim += 1

    if avalia_resultado(tab=tab):   # Parar se alguem ganhou
        break
    elif fim == 0:                # Parar se houver empate
        print('Houve um empate!')
        break

    # Entrando com as jogadas
    linha = int(input("Informe a linha da jogada: "))
    coluna = int(input("Informe a coluna da jogada: "))
    jogada = str(input("Informe sua jogada: ")).lower()

    if validar(linha, coluna, jogada):  # validadno jogadas de acordo com as regras
        if tab[linha][coluna] == 0:
            tab[linha][coluna] = jogada
        else:
            print('Campo já preenchido!')
    else:
        print('Jogada inválida.\nOs valores de linha/coluna devem ser 0, 1 ou 2.\nAs jogadas são com X ou O')

