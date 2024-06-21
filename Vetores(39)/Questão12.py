valores = []

for i in range(5):
    valor = float(input(f"Digite o valor {i+1}: "))
    valores.append(valor)

maior_valor = max(valores)
menor_valor = min(valores)
media_valores = sum(valores) / len(valores)

print("Valores lidos:", valores)
print(f"Maior valor: {maior_valor}")
print(f"Menor valor: {menor_valor}")
print(f"Média dos valores: {media_valores:.2f}")
