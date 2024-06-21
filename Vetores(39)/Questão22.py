vetor1 = []
print("Digite 10 valores para o primeiro vetor:")
for i in range(10):
    valor = int(input(f"Valor {i + 1} do primeiro vetor: "))
    vetor1.append(valor)

vetor2 = []
print("Digite 10 valores para o segundo vetor:")
for i in range(10):
    valor = int(input(f"Valor {i + 1} do segundo vetor: "))
    vetor2.append(valor)

novo_vetor = []
for i in range(10):
    if i % 2 == 0:
        novo_vetor.append(vetor1[i])
    else:
        novo_vetor.append(vetor2[i])

print("Novo vetor:", novo_vetor)
