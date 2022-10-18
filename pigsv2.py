from tabulate import tabulate
import copy

tamanho = 4
tabuleiro = [["x" for _ in range(tamanho)] for _ in range(tamanho)]

tabuleirosDasSolucoesDiferentes = []

maximoDePorcos = 4

colunas = set()
diagonaisPositivas = set()
diagonaisNegativas = set()


def rainhasDiferenciado(linha, maximoDePorcos, porcosNoTabuleiro=0):
    if maximoDePorcos == porcosNoTabuleiro:
        tabuleirosDasSolucoesDiferentes.append(copy.deepcopy(tabuleiro))
        return

    for coluna in range(len(tabuleiro)):
        if coluna in colunas or (linha + coluna) in diagonaisPositivas or (linha - coluna) in diagonaisNegativas:
            continue
        
        colunas.add(coluna)
        diagonaisPositivas.add(linha + coluna)
        diagonaisNegativas.add(linha - coluna)
        tabuleiro[linha][coluna] = "Q"

        rainhasDiferenciado(linha + 1, maximoDePorcos, porcosNoTabuleiro + 1)
        
        colunas.remove(coluna)
        diagonaisPositivas.remove(linha + coluna)
        diagonaisNegativas.remove(linha - coluna)
        tabuleiro[linha][coluna] = "x"
        

rainhasDiferenciado(0, 4)

for tabuleiro in tabuleirosDasSolucoesDiferentes:
    print(tabulate(tabuleiro, tablefmt='fancy_grid'))
print("formas:", len(tabuleirosDasSolucoesDiferentes))
