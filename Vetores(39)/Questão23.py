conjunto_x = []
print("Digite 5 números reais para o conjunto X:")
for i in range(5):
    numero = float(input(f"X{i + 1}: "))
    conjunto_x.append(numero)

conjunto_y = []
print("Digite 5 números reais para o conjunto Y:")
for i in range(5):
    numero = float(input(f"Y{i + 1}: "))
    conjunto_y.append(numero)

produto_escalar = sum(x * y for x, y in zip(conjunto_x, conjunto_y))

print("Conjunto X:", conjunto_x)
print("Conjunto Y:", conjunto_y)
print("Produto escalar:", produto_escalar)
