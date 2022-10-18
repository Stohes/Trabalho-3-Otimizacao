from tabulate import tabulate
import copy


def resolucao(tabuleiro, maximoDePorcosNoTabuleiro, linha=0, porcosNoTabuleiro=0):
    global formas
    
    if porcosNoTabuleiro == maximoDePorcosNoTabuleiro:
        formas += 1
        tabuleirosDasFormas.append(copy.deepcopy(tabuleiro))
    
    for coluna in range(len(tabuleiro)):
        if seguro(tabuleiro, linha, coluna):
            
            tabuleiro[linha][coluna] = 1
            resolucao(tabuleiro, maximoDePorcosNoTabuleiro, linha + 1, porcosNoTabuleiro + 1)
            tabuleiro[linha][coluna] = 0
            
            
def seguro(tabuleiro, linha, coluna):
    
    col = coluna
    lin = linha
    
    try:
        if tabuleiro[linha][coluna] == 1:
            return False
    except Exception as e:
        return False
    
    try:
        if 1 in tabuleiro[linha]:
            return False
    except Exception as e:
        return False
    
    for linh in range(len(tabuleiro)):
        if tabuleiro[linh][coluna] == 1:
            return False
        
    while lin >= 0 and col >= 0:  # cima esquerda
        if tabuleiro[lin][col] == 1:
            return False
        lin -= 1
        col -= 1
    lin = linha
    col = coluna

    while lin >= 0 and col <= len(tabuleiro) - 1:  # cima direita
        if tabuleiro[lin][col] == 1:
            return False
        lin -= 1
        col += 1
    lin = linha
    col = coluna

    while lin <= len(tabuleiro) - 1 and col <= len(tabuleiro) - 1:  # baixo direita
        if tabuleiro[lin][col] == 1:
            return False
        lin += 1
        col += 1
    lin = linha
    col = coluna

    while lin <= len(tabuleiro) - 1 and col >= 0:  # baixo esquerda
        if tabuleiro[lin][col] == 1:
            return False
        lin += 1
        col -= 1
    lin = linha
    col = coluna
    
    return True


formas = 0
tabuleirosDasFormas = []

tamanho = 4
tabuleiro = [[0 for _ in range(tamanho)] for _ in range(tamanho)]


resolucao(tabuleiro, 2)

# for linha in range(len(tabuleiro)):
#     resolucao(tabuleiro, 2, linha)
    
# for porcosNoTabuleiro in range(1, 5):
#     for linha in range(len(tabuleiro)):
#         resolucao(tabuleiro, porcosNoTabuleiro, linha)
        
for tabuleiro in tabuleirosDasFormas:
    print(tabulate(tabuleiro, tablefmt='fancy_grid'))
print("formas:", formas)

#TODO criar o tabuleiro a partir da linha de comando (passa 4 cria tabuleiro 4x4)
#TODO criar funcao auxiliar para colocar as rainhas,
# mudar no tabuleiro as casas atacadas para -1
# pode remover a seguro() depois disso, é só verificar se é um -1 como primeira 
# condicao de parada da recursao (usar os loops da seguro() como base), pode ser 
# que fique pior
