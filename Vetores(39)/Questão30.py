
vetor_a = []
vetor_b = []

print("Digite 10 elementos para o vetor A:")
for i in range(10):
    elemento = int(input(f"Elemento {i+1} de A: "))
    vetor_a.append(elemento)

print("\nDigite 10 elementos para o vetor B:")
for i in range(10):
    elemento = int(input(f"Elemento {i+1} de B: "))
    vetor_b.append(elemento)

vetor_interseccao = list(set(vetor_a) & set(vetor_b))

print("\nVetor de interseção entre A e B:", vetor_interseccao)
