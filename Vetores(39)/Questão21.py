vetor_a = []
print("Digite 10 números inteiros para o vetor A:")
for i in range(10):
    numero = int(input(f"A{i + 1}: "))
    vetor_a.append(numero)

vetor_b = []
print("Digite 10 números inteiros para o vetor B:")
for i in range(10):
    numero = int(input(f"B{i + 1}: "))
    vetor_b.append(numero)

vetor_c = [a - b for a, b in zip(vetor_a, vetor_b)]

print("Vetor C (A - B):", vetor_c)
