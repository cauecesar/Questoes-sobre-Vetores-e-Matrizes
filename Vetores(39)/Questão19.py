vetor = [(i + 5 * i) % (i + 1) for i in range(50)]

for i in range(50):
    print(f"vetor[{i}] = {vetor[i]}")
