from tabulate import tabulate
import copy

tamanho = 4
porcosDesejados = 2
galinhasDesejadas = 0

tabuleiro = [["" for _ in range(tamanho)] for _ in range(tamanho)]
tabuleirosDasSolucoesDiferentes = []


linhasAtacadasPorPorcos = []
colunasAtacadasPorPorcos = []
diagonaisPositivasAtacadasPorPorcos = []
diagonaisNegativasAtacadasPorPorcos = []


def rainhasDiferenciado(porcosDesejados, galinhasDesejadas, porcosNoTabuleiro=0, galinhasNoTabuleiro=0):

    if porcosDesejados == porcosNoTabuleiro and galinhasDesejadas == galinhasNoTabuleiro:
        if tabuleiro not in tabuleirosDasSolucoesDiferentes:
            tabuleirosDasSolucoesDiferentes.append(copy.deepcopy(tabuleiro))
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

                rainhasDiferenciado(
                    porcosDesejados, galinhasDesejadas, porcosNoTabuleiro + 1, galinhasNoTabuleiro)

                linhasAtacadasPorPorcos.remove(linha)
                colunasAtacadasPorPorcos.remove(coluna)
                diagonaisPositivasAtacadasPorPorcos.remove(linha + coluna)
                diagonaisNegativasAtacadasPorPorcos.remove(linha - coluna)
                tabuleiro[linha][coluna] = ""


rainhasDiferenciado(porcosDesejados, galinhasDesejadas)

for tabuleiro in tabuleirosDasSolucoesDiferentes:
    print(tabulate(tabuleiro, tablefmt='fancy_grid'))

# print(tabulate(tabuleirosDasSolucoesDiferentes[len(tabuleirosDasSolucoesDiferentes) - 1], tablefmt='fancy_grid'))

print("formas:", len(tabuleirosDasSolucoesDiferentes))
