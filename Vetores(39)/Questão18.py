vetor = []
print("Digite 10 números:")
for i in range(10):
    numero = int(input(f"Número {i + 1}: "))
    vetor.append(numero)

x = int(input("Digite um número inteiro x: "))

multiplos_de_x = [numero for numero in vetor if numero % x == 0]
print(f"Múltiplos de {x} no vetor:", multiplos_de_x)
