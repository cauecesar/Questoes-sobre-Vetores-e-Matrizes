numeros_reais = []

for i in range(10):
    numero = float(input(f"Digite o número real {i+1}: "))
    numeros_reais.append(numero)

quantidade_negativos = len([num for num in numeros_reais if num < 0])
soma_positivos = sum(num for num in numeros_reais if num > 0)

print(f"Quantidade de números negativos: {quantidade_negativos}")
print(f"Soma dos números positivos: {soma_positivos}")
