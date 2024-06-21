def ler_matriz():
    return [[float(input(f'Elemento [{i+1}][{j+1}]: ')) for j in range(3)] for i in range(3)]

def multiplicar_matrizes(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]

def imprimir_matriz(B):
    print("Matriz resultante B = A^2:")
    for linha in B:
        print(linha)

print("Digite os elementos da matriz A:")
A = ler_matriz()

B = multiplicar_matrizes(A, A)

imprimir_matriz(B)
