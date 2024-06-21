matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposta = [[matriz[j][i] for j in range(3)] for i in range(3)]

for linha in transposta:
    print(linha)

