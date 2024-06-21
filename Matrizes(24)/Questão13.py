import random

matriz = [[random.randint(1, 20) for _ in range(4)] for _ in range(4)]

print("Matriz original:")
for linha in matriz:
    print(linha)

for i in range(4):
    for j in range(i+1, 4):
        matriz[i][j] = 0

print("\nMatriz triangular inferior:")
for linha in matriz:
    print(linha)
