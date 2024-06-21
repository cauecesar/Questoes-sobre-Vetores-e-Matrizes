def imprimir_triangulo_pascal(n):
    linha = [1]
    for _ in range(n):
        print(' '.join(map(str, linha)))
        nova_linha = [1]
        for i in range(len(linha) - 1):
            nova_linha.append(linha[i] + linha[i + 1])
        nova_linha.append(1)
        linha = nova_linha

n = int(input("Digite o número de linhas para o Triângulo de Pascal: "))
imprimir_triangulo_pascal(n)
