vetor = []
print("Digite 15 elementos para o vetor:")
for i in range(15):
    elemento = int(input())
    vetor.append(elemento)

vetor_compactado = [elemento for elemento in vetor if elemento != 0]

print("Vetor compactado:", vetor_compactado)
