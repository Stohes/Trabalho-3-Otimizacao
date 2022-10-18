from tabulate import tabulate
import copy

tamanho = 4
tabuleiro = [["x" for _ in range(tamanho)] for _ in range(tamanho)]

tabuleirosDasSolucoesDiferentes = []

porcosDesejados = 4
galinhasDesejadas = 4

linhasPorcos = set()
colunasPorcos = set()
diagonaisPositivasPorcos = set()
diagonaisNegativasPorcos = set()

linhasGalinhas = set()
colunasGalinhas = set()
diagonaisPositivasGalinhas = set()
diagonaisNegativasGalinhas = set()


def rainhasDiferenciado(porcosDesejados, galinhasDesejadas, porcosNoTabuleiro=0, galinhasNoTabuleiro=0):
    if porcosDesejados == porcosNoTabuleiro and galinhasDesejadas == galinhasNoTabuleiro:
        if tabuleiro not in tabuleirosDasSolucoesDiferentes:
            tabuleirosDasSolucoesDiferentes.append(copy.deepcopy(tabuleiro))
            return
    
    if porcosNoTabuleiro < porcosDesejados:
        for linha in range(len(tabuleiro)):
            if linha in linhasPorcos:
                continue
            for coluna in range(len(tabuleiro)):
                if coluna in colunasPorcos or (linha + coluna) in diagonaisPositivasPorcos or (linha - coluna) in diagonaisNegativasPorcos:
                    continue
                
                linhasPorcos.add(linha)
                colunasPorcos.add(coluna)
                diagonaisPositivasPorcos.add(linha + coluna)
                diagonaisNegativasPorcos.add(linha - coluna)
                tabuleiro[linha][coluna] = "P"

                rainhasDiferenciado(porcosDesejados, galinhasDesejadas, porcosNoTabuleiro + 1, galinhasNoTabuleiro)
                
                linhasPorcos.remove(linha)
                colunasPorcos.remove(coluna)
                diagonaisPositivasPorcos.remove(linha + coluna)
                diagonaisNegativasPorcos.remove(linha - coluna)
                tabuleiro[linha][coluna] = "x"

    if porcosDesejados == porcosNoTabuleiro and galinhasNoTabuleiro < galinhasDesejadas:
        for linha in range(len(tabuleiro)):
            if linha in linhasGalinhas:
                continue
            for coluna in range(len(tabuleiro)):
                if tabuleiro[linha][coluna] == "P" or coluna in colunasGalinhas or (linha + coluna) in diagonaisPositivasGalinhas or (linha - coluna) in diagonaisNegativasGalinhas:
                    continue
                
                linhasGalinhas.add(linha)
                colunasGalinhas.add(coluna)
                diagonaisPositivasGalinhas.add(linha + coluna)
                diagonaisNegativasGalinhas.add(linha - coluna)
                tabuleiro[linha][coluna] = "G"

                rainhasDiferenciado(porcosDesejados, galinhasDesejadas, porcosNoTabuleiro, galinhasNoTabuleiro + 1)
                
                linhasGalinhas.remove(linha)
                colunasGalinhas.remove(coluna)
                diagonaisPositivasGalinhas.remove(linha + coluna)
                diagonaisNegativasGalinhas.remove(linha - coluna)
                tabuleiro[linha][coluna] = "x"
        

rainhasDiferenciado(porcosDesejados, galinhasDesejadas)

for tabuleiro in tabuleirosDasSolucoesDiferentes:
    print(tabulate(tabuleiro, tablefmt='fancy_grid'))
print("formas:", len(tabuleirosDasSolucoesDiferentes))
