tamanho = 10

matriz = [[0] * tamanho for _ in range(tamanho)]

for i in range(tamanho):
    for j in range(tamanho):
        if i < j:
            matriz[i][j] = 2*i + 7*j**2
        elif i == j:
            matriz[i][j] = 3*i**2 + 1
        else: # i > j
            matriz[i][j] = 4*i**3 - 5*j**2 + 1

for linha in matriz:
    print(linha)
