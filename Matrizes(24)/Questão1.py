matriz = [
    [11, 2, 13, 14],
    [15, 6, 17, 18],
    [19, 10, 21, 22],
    [23, 24, 25, 26]
]

valores_maior_que_dez = sum(valor > 10 for linha in matriz for valor in linha)

print(f"A matriz possui {valores_maior_que_dez} valores maiores que 10.")
