import random

numeros_unicos = random.sample(range(100), 25)

cartela = [numeros_unicos[i:i+5] for i in range(0, 25, 5)]

print("Cartela de Bingo:")
for linha in cartela:
    print(linha)
