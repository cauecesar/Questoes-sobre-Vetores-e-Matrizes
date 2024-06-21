matriz = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

x = int(input("Digite o valor de X: "))

localizacao = None
for i in range(5):
    for j in range(5):
        if matriz[i][j] == x:
            localizacao = (i, j)
            break
    if localizacao:
        break

if localizacao:
    print(f"Valor {x} encontrado na linha {localizacao[0]} e coluna {localizacao[1]}.")
else:
    print("Valor não encontrado.")
