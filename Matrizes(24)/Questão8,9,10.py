matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

soma = sum(matriz[i][j] for i in range(3) for j in range(i+1, 3))

print(f"A soma dos elementos acima da diagonal principal é {soma}.")
