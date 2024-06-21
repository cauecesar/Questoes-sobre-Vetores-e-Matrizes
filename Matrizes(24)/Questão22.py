def ler_matriz():
    return [[float(input(f'Elemento [{i+1}][{j+1}]: ')) for j in range(3)] for i in range(3)]

def multiplicar_matrizes(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]

def imprimir_matriz(C):
    print("Matriz resultante C = A * B:")
    for linha in C:
        print(linha)

print("Digite os elementos da matriz A:")
A = ler_matriz()
print("Digite os elementos da matriz B:")
B = ler_matriz()

C = multiplicar_matrizes(A, B)

imprimir_matriz(C)