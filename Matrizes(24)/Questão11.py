matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

soma = sum(matriz[i][2-i] for i in range(3))

print(f"A soma dos elementos na diagonal secundária é {soma}.")
