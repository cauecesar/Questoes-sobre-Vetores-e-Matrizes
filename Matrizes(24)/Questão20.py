
matriz = [
    [1.5, 2.5, 3.5, 4.5, 5.5, 6.5],
    [7.5, 8.5, 9.5, 10.5, 11.5, 12.5],
    [13.5, 14.5, 15.5, 16.5, 17.5, 18.5]
]

soma_colunas_impares = sum(matriz[i][j] for i in range(3) for j in range(0, 6, 2))
print("Soma dos elementos das colunas ímpares:", soma_colunas_impares)

media_colunas_2_4 = sum(matriz[i][1] + matriz[i][3] for i in range(3)) / (3 * 2)
print("Média aritmética dos elementos da segunda e quarta colunas:", media_colunas_2_4)

for i in range(3):
    matriz[i][5] = matriz[i][0] + matriz[i][1]

print("Matriz modificada:")
for linha in matriz:
    print(linha)
