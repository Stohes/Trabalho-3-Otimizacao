# from tabulate import tabulate
import copy
import sys
import math

# tamanho = int(sys.argv[1])

# num1 = int(sys.argv[2])
# num2 = int(sys.argv[3])

tamanho = 8

num1 = 3
num2 = 4

porcosDesejados = min(num1, num2)
galinhasDesejadas = max(num1, num2)

tabuleiro = [["" for _ in range(tamanho)] for _ in range(tamanho)]
tabuleirosDasSolucoesDiferentes = []


linhasAtacadasPorPorcos = []
colunasAtacadasPorPorcos = []
diagonaisPositivasAtacadasPorPorcos = []
diagonaisNegativasAtacadasPorPorcos = []



def rainhasDiferenciado(porcosDesejados, galinhasDesejadas, porcosNoTabuleiro=0):

    global resultado
    if porcosDesejados == porcosNoTabuleiro:
        casinhasSafe = 0


        for linha in range(len(tabuleiro)):
            if linha in linhasAtacadasPorPorcos:
                continue
            for coluna in range(len(tabuleiro)):
                if coluna in colunasAtacadasPorPorcos:
                    continue

                if tabuleiro[linha][coluna] == "P" or (linha + coluna) in diagonaisPositivasAtacadasPorPorcos or (linha - coluna) in diagonaisNegativasAtacadasPorPorcos:
                    continue

                casinhasSafe += 1

        resultado += math.comb(casinhasSafe, galinhasDesejadas)
        return

    if porcosNoTabuleiro < porcosDesejados:
        for linha in range(len(tabuleiro)):
            for coluna in range(len(tabuleiro)):
                if tabuleiro[linha][coluna] == "P":
                    continue

                linhasAtacadasPorPorcos.append(linha)
                colunasAtacadasPorPorcos.append(coluna)
                diagonaisPositivasAtacadasPorPorcos.append(linha + coluna)
                diagonaisNegativasAtacadasPorPorcos.append(linha - coluna)
                tabuleiro[linha][coluna] = "P"

                rainhasDiferenciado(porcosDesejados, galinhasDesejadas, porcosNoTabuleiro + 1)

                linhasAtacadasPorPorcos.remove(linha)
                colunasAtacadasPorPorcos.remove(coluna)
                diagonaisPositivasAtacadasPorPorcos.remove(linha + coluna)
                diagonaisNegativasAtacadasPorPorcos.remove(linha - coluna)
                tabuleiro[linha][coluna] = ""



resultado = 0

rainhasDiferenciado(porcosDesejados, galinhasDesejadas)

# for tabuleiro in tabuleirosDasSolucoesDiferentes:
#     print(tabulate(tabuleiro, tablefmt='fancy_grid'))

# print(tabulate(tabuleirosDasSolucoesDiferentes[len(tabuleirosDasSolucoesDiferentes) - 1], tablefmt='fancy_grid'))

# print("formas:", len(tabuleirosDasSolucoesDiferentes))



print(resultado)