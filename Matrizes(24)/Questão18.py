matriz = [
    [5, -8, 10],
    [1, 2, 15],
    [25, 10, 7]
]

soma_colunas = [sum(linha[i] for linha in matriz) for i in range(3)]

print("Array resultante pela soma das colunas:", soma_colunas)
