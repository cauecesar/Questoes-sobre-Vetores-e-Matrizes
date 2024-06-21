matriz1 = [
    [1, 20, 3, 4],
    [5, 6, 70, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

matriz2 = [
    [17, 2, 19, 20],
    [21, 22, 7, 24],
    [25, 26, 27, 28],
    [29, 30, 31, 32]
]

matriz3 = [[max(matriz1[i][j], matriz2[i][j]) for j in range(4)] for i in range(4)]

for linha in matriz3:
    print(linha)

