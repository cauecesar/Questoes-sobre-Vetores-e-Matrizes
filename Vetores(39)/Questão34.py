vetor = []

print("Digite 10 números diferentes:")
while len(vetor) < 10:
    numero = int(input("Digite um número: "))
    if numero not in vetor:
        vetor.append(numero)
    else:
        print("Número já foi digitado, por favor insira um número diferente.")

print("Vetor final:", vetor)
