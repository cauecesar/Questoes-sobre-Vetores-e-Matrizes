vetor = []
print("Digite 20 números inteiros:")
for i in range(20):
    numero = int(input(f"Número {i + 1}: "))
    vetor.append(numero)

vetor_unico = list(set(vetor))

print("Elementos do vetor sem repetições:", vetor_unico)
