

class Game():

    def __init__(self):
        self.tabuleiro = [['_' for _ in range(3)] for _ in range(3)]

    def interface(self):
        for tab in self.tabuleiro:
            for i, t in enumerate(tab):
                print(t, end='')
                if i < 2:
                    print('|', end='')
            print()

    def jogada(self, lin, col, valor):
        self.linha = lin
        self.coluna = col
        self.jogada = valor

        if self.validar_jogada():
            self.tabuleiro[self.linha][self.coluna] = self.jogada
        self.interface()

    def fim_de_jogo(self):
        if self.Analisa_Resultado():
            return False
        else:
            return True

    def validar_jogada(self):

        if 0 <= self.linha <= 2 and 0 <= self.coluna <= 2:
            if self.jogada == 'x' or self.jogada == 'o':
                return True
            else:
                print('Jogada inválida! As jogada válidas são X ou O.')
                return False
        else:
            print('''Você não informou valores de linh/coluna corretos!
            Informe valores os 0, 1 ou 2 como no enunciado''')
            return False

    def Analisa_Resultado(self):

        for tab in self.tabuleiro:
            if tab.count('x') == 3:
                print('X venceu!')
                return True
            elif tab.count('o') == 3:
                print('O venceu!')
                return True

        for i in range(3):
            if self.tabuleiro[0][i] == self.tabuleiro[1][i] == self.tabuleiro[2][i] != '_':
                if self.tabuleiro[0][i] == 'x':
                    print('X venceu!')
                if self.tabuleiro[0][i] == 'o':
                    print('O venceu')
                return True

        if self.tabuleiro[1][1] != '_':
            if (self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2]) or (self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0]):
                if self.tabuleiro[1][1] == 'x':
                    print('X venceu')
                else:
                    print('O venceu')
                return True

        return False



            # Iniciar Jogo

# Instanciar o jogo
game = Game()
# Criar interface
game.interface()

# Iniciando jogada
while game.fim_de_jogo():

    try:
        linha = int(input('Informe a linha de sua jogada: '))
        coluna = int(input('Informe a coluna de sua jogada: '))
        jogada = str(input('Informe sua jogada [X ou O]: ')).strip().lower()
    except:
        print('Você informou valores errados, analise suas jogadas')
        print('Valores para linha e coluna: 0, 1 ou 2')
        print('Valores para jogadas: X ou O')
    else:
        game.jogada(linha, coluna, jogada)
