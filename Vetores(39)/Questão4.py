vetor = []

for i in range(8):
    valor = int(input(f"Digite o valor {i+1} do vetor: "))
    vetor.append(valor)

X = int(input("Digite a posição X (entre 1 e 8): ")) - 1
Y = int(input("Digite a posição Y (entre 1 e 8): ")) - 1

if X >= 0 and X < 8 and Y >= 0 and Y < 8:
    soma = vetor[X] + vetor[Y]
    print(f"A soma dos valores nas posições {X+1} e {Y+1} é: {soma}")
else:
    print("Posições inválidas. Por favor, escolha posições entre 1 e 8.")
