
valores = []


for i in range(6):
    valor = int(input(f"Digite o valor {i+1}: "))
    valores.append(valor)


print("Os valores lidos são:")
for valor in valores:
    print(valor)