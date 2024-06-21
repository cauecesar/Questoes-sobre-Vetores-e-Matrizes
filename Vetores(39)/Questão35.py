def numero_para_vetor(numero):
    return [int(digito) for digito in str(numero)[::-1]]

def soma_vetores(vetor_a, vetor_b):
    tamanho_maximo = max(len(vetor_a), len(vetor_b))
    vetor_soma = []
    carry = 0
    for i in range(tamanho_maximo):
        soma = carry
        if i < len(vetor_a):
            soma += vetor_a[i]
        if i < len(vetor_b):
            soma += vetor_b[i]
        vetor_soma.append(soma % 10)
        carry = soma // 10
    if carry:
        vetor_soma.append(carry)
    return vetor_soma

a = int(input("Digite um número positivo menor que 10000 para 'a': "))
b = int(input("Digite um número positivo menor que 10000 para 'b': "))

vetor_a = numero_para_vetor(a)
vetor_b = numero_para_vetor(b)

vetor_soma = soma_vetores(vetor_a, vetor_b)

print("Vetor de 'a':", vetor_a)
print("Vetor de 'b':", vetor_b)
print("Vetor da soma de 'a' e 'b':", vetor_soma)
