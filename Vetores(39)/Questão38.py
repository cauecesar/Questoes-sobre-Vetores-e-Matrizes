vetor = []

print("Digite dez valores numéricos:")
for _ in range(10):
    valor = float(input("Digite um valor: "))

    indice = 0
    while indice < len(vetor) and vetor[indice] < valor:
        indice += 1
    vetor.insert(indice, valor)

print("Valores em ordem crescente:", vetor)

