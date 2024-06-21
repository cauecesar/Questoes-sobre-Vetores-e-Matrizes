numeros_reais = []

quadrados = []

for i in range(10):
    numero = float(input(f"Digite o número real {i+1}: "))
    numeros_reais.append(numero)
    quadrados.append(numero**2)

print("Números reais:")
for numero in numeros_reais:
    print(numero)

print("Quadrado dos números:")
for quadrado in quadrados:
    print(quadrado)
