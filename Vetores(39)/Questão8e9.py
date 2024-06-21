valores = []

for i in range(6):
    valor = int(input(f"Digite o valor {i+1}: "))
    valores.append(valor)

print("Os valores na ordem inversa são:")
for valor in reversed(valores):
    print(valor)

