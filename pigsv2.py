from tabulate import tabulate
import copy

tamanho = 4
tabuleiro = [["x" for _ in range(tamanho)] for _ in range(tamanho)]

tabuleirosDasSolucoesDiferentes = []

porcosDesejados = 2

linhas = set()
colunas = set()
diagonaisPositivas = set()
diagonaisNegativas = set()


def rainhasDiferenciado(porcosDesejados, porcosNoTabuleiro=0):
    if porcosDesejados == porcosNoTabuleiro:
        if tabuleiro not in tabuleirosDasSolucoesDiferentes:
            tabuleirosDasSolucoesDiferentes.append(copy.deepcopy(tabuleiro))
            return
    
    for linha in range(len(tabuleiro)):
        for coluna in range(len(tabuleiro)):
            if linha in linhas or coluna in colunas or (linha + coluna) in diagonaisPositivas or (linha - coluna) in diagonaisNegativas:
                continue
            
            linhas.add(linha)
            colunas.add(coluna)
            diagonaisPositivas.add(linha + coluna)
            diagonaisNegativas.add(linha - coluna)
            tabuleiro[linha][coluna] = "Q"

            rainhasDiferenciado(porcosDesejados, porcosNoTabuleiro + 1)
            
            linhas.remove(linha)
            colunas.remove(coluna)
            diagonaisPositivas.remove(linha + coluna)
            diagonaisNegativas.remove(linha - coluna)
            tabuleiro[linha][coluna] = "x"
        

rainhasDiferenciado(porcosDesejados)

for tabuleiro in tabuleirosDasSolucoesDiferentes:
    print(tabulate(tabuleiro, tablefmt='fancy_grid'))
print("formas:", len(tabuleirosDasSolucoesDiferentes))
