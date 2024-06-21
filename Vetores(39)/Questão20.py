vetor1 = []
print("Digite 10 números inteiros no intervalo [0,50]:")
for i in range(10):
    while True:
        numero = int(input(f"Número {i + 1}: "))
        if 0 <= numero <= 50:
            vetor1.append(numero)
            break
        else:
            print("Número fora do intervalo. Tente novamente.")

vetor2 = [numero for numero in vetor1 if numero % 2 != 0]

print("Vetor 1:")
for i in range(0, len(vetor1), 2):
    print(vetor1[i], vetor1[i + 1] if i + 1 < len(vetor1) else '')

print("Vetor 2:")
for i in range(0, len(vetor2), 2):
    print(vetor2[i], vetor2[i + 1] if i + 1 < len(vetor2) else '')

