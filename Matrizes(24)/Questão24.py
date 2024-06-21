def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(' '.join(str(x) for x in linha))

def verificar_vitoria(tabuleiro, jogador):
    
    for i in range(3):
        if all(tabuleiro[i][j] == jogador for j in range(3)) or \
           all(tabuleiro[j][i] == jogador for j in range(3)):
            return True
    if tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador or \
       tabuleiro[0][2] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][0] == jogador:
        return True
    return False

def verificar_empate(tabuleiro):
    return all(tabuleiro[i][j] != 0 for i in range(3) for j in range(3))

def melhor_jogada(tabuleiro, jogador):

    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == 0:
                tabuleiro[i][j] = jogador
                if verificar_vitoria(tabuleiro, jogador):
                    return (i, j)
                tabuleiro[i][j] = 0

    for i in [0, 2]:
        for j in [0, 2]:
            if tabuleiro[i][j] == 0:
                return (i, j)

    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == 0:
                return (i, j)

tabuleiro = [
    [-1, 1, 1],
    [-1, -1, 0],
    [0, 1, 0]
]

jogada = melhor_jogada(tabuleiro, -1)
if jogada:
    print(f"A melhor jogada é na posição: {jogada}")
else:
    print("Não há jogadas disponíveis.")
