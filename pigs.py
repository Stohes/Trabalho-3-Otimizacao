from tabulate import tabulate
import copy
# tabuleiro = [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]
# tabuleiro2 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
# tabuleiro3 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
formas = 0
tabuleirosDasFormas = []

def resolucao(tabuleiro, linha):
    global formas
    if linha >= len(tabuleiro):
        formas += 1
        tabuleirosDasFormas.append(copy.deepcopy(tabuleiro))
    
    for coluna in range(len(tabuleiro)):
        
        if seguro(tabuleiro, linha, coluna):
            tabuleiro[linha][coluna] = 1
            
            if resolucao(tabuleiro, linha + 1):
                return True
            
            tabuleiro[linha][coluna] = 0
            
    return False
            
            
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


teste = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

# print(tabulate(teste, tablefmt='fancy_grid'))

resolucao(teste, 0)
for tabuleiro in tabuleirosDasFormas:
    print(tabulate(tabuleiro, tablefmt='fancy_grid'))
print("formas:", formas)
