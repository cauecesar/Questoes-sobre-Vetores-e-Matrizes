matriz = [
    [16, 2, 3, 14],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 20, 15, 4]
]

for linha in matriz:
    print(linha)

maior_valor = max(max(linha) for linha in matriz)
localizacao = [(i, linha.index(maior_valor)) for i, linha in enumerate(matriz) if maior_valor in linha][0]

print(f"O maior valor é {maior_valor} e está localizado na linha {localizacao[0]} e coluna {localizacao[1]}.")

