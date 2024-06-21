vetor = []

for i in range(10):
    valor = int(input(f"Digite o valor {i+1}: "))
    vetor.append(valor)

valores_pares = [valor for valor in vetor if valor % 2 == 0]
quantidade_pares = len(valores_pares)

print(f"O vetor possui {quantidade_pares} valores pares.")
