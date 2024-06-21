vetor = []

for i in range(10):
    valor = int(input(f"Digite o valor {i+1}: "))
    vetor.append(valor)

valores_iguais = set([valor for valor in vetor if vetor.count(valor) > 1])

if valores_iguais:
    print("Valores iguais encontrados no vetor:", valores_iguais)
else:
    print("Não foram encontrados valores iguais no vetor.")
