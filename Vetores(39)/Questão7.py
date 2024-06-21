vetor = []

for i in range(10):
    numero = int(input(f"Digite o número inteiro {i+1}: "))
    vetor.append(numero)

maior_elemento = max(vetor)
posicao_maior_elemento = vetor.index(maior_elemento)

print("Vetor:", vetor)
print(f"O maior elemento é {maior_elemento} e está na posição {posicao_maior_elemento}.")
