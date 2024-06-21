vetor = []
numero = 1

while len(vetor) < 100:
    if numero % 7 != 0 and str(numero)[-1] != '7':
        vetor.append(numero)
    numero += 1

print("Vetor:", vetor)

