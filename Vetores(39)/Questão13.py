valores = []

for i in range(5):
    valor = float(input(f"Digite o valor {i+1}: "))
    valores.append(valor)

maior_valor = max(valores)
menor_valor = min(valores)
posicao_maior = valores.index(maior_valor)
posicao_menor = valores.index(menor_valor)

print(f"O maior valor está na posição {posicao_maior} e o menor na posição {posicao_menor}.")

