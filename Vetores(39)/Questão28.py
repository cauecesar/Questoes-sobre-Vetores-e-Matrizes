
vetor_v = []


vetor_v1 = []
vetor_v2 = []

print("Digite 10 números inteiros para o vetor v:")
for i in range(10):
    numero = int(input(f"Digite o número {i+1}: "))
    vetor_v.append(numero)
    if numero % 2 == 0:
        vetor_v2.append(numero)
    else:
        vetor_v1.append(numero)

print("\nElementos utilizados de v1 (ímpares):", vetor_v1)
print("Elementos utilizados de v2 (pares):", vetor_v2)

