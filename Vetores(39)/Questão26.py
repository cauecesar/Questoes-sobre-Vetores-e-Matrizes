import math

vetor_v = []

print("Digite 10 números para o vetor v:")
for i in range(10):
    numero = float(input(f"Digite o número {i+1}: "))
    vetor_v.append(numero)

media = sum(vetor_v) / len(vetor_v)

soma_dos_quadrados = sum((x - media) ** 2 for x in vetor_v)
desvio_padrao = math.sqrt(soma_dos_quadrados / len(vetor_v))

print(f"\nMédia do vetor: {media}")
print(f"Desvio padrão: {desvio_padrao}")

