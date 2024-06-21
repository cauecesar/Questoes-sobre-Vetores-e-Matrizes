
numeros_pares = []
numeros_impares = []

print("Digite 6 números inteiros:")
for i in range(6):
    numero = int(input(f"Digite o número {i+1}: "))
    if numero % 2 == 0:
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)

soma_pares = sum(numeros_pares)
quantidade_impares = len(numeros_impares)

print("\nNúmeros pares digitados:", numeros_pares)
print("Soma dos números pares digitados:", soma_pares)
print("Números ímpares digitados:", numeros_impares)
print("Quantidade de números ímpares digitados:", quantidade_impares)
