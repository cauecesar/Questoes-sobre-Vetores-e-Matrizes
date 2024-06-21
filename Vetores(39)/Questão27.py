def eh_primo(num):
    """Função para verificar se um número é primo."""
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

vetor = []

print("Digite 10 números inteiros:")
for i in range(10):
    numero = int(input(f"Digite o número {i+1}: "))
    vetor.append(numero)

print("\nNúmeros primos no vetor:")
for i, numero in enumerate(vetor):
    if eh_primo(numero):
        print(f"O número {numero} na posição {i} é primo.")
