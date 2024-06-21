vetor = []
print("Digite 10 números:")
for i in range(10):
    numero = int(input(f"Número {i + 1}: "))
    vetor.append(numero)

vetor = [0 if numero < 0 else numero for numero in vetor]

print("Vetor após atribuir 0 aos valores negativos:", vetor)
