vetor = []
print("Digite 5 números reais:")
for i in range(5):
    numero = float(input(f"Número {i + 1}: "))
    vetor.append(numero)

codigo = int(input("Digite o código inteiro (0 para finalizar, 1 para ordem direta, 2 para ordem inversa): "))

if codigo == 0:
    print("Programa finalizado.")
elif codigo == 1:
    print("Vetor na ordem direta:", vetor)
elif codigo == 2:
    print("Vetor na ordem inversa:", vetor[::-1])
else:
    print("Código inválido.")
