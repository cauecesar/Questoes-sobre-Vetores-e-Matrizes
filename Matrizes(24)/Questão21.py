def imprimir_matrizes(*matrizes):
    for idx, matriz in enumerate(matrizes, start=1):
        print(f"Matriz {idx}:")
        for linha in matriz:
            print(linha)
        print()

def somar_matrizes(matriz1, matriz2):
  
    resultado = [[0]*3 for _ in range(3)]
    
    for i in range(2):
        for j in range(2):
            resultado[i][j] = matriz1[i][j] + matriz2[i][j]
    return resultado

def subtrair_matrizes(matriz1, matriz2):
   
    resultado = [[0]*3 for _ in range(3)]
    
    for i in range(2):
        for j in range(2):
            resultado[i][j] = matriz1[i][j] - matriz2[i][j]
    return resultado

def adicionar_constante(matriz, constante):

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz[i][j] += constante

matriz1 = [
    [1.0, 2.0],
    [3.0, 4.0]
]

matriz2 = [
    [5.0, 6.0],
    [7.0, 8.0]
]

while True:
    print("\nMenu de opções:")
    print("(a) Somar as duas matrizes")
    print("(b) Subtrair a primeira matriz da segunda")
    print("(c) Adicionar uma constante às duas matrizes")
    print("(d) Imprimir as matrizes")
    print("(e) Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == 'a':
        resultado = somar_matrizes(matriz1, matriz2)
        imprimir_matrizes(resultado)

    elif opcao == 'b':
        resultado = subtrair_matrizes(matriz1, matriz2)
        imprimir_matrizes(resultado)

    elif opcao == 'c':
        constante = float(input("Digite a constante: "))
        adicionar_constante(matriz1, constante)
        adicionar_constante(matriz2, constante)

    elif opcao == 'd':
        imprimir_matrizes(matriz1, matriz2)

    elif opcao == 'e':
        break
