x = []
print("Digite 5 elementos para o vetor x:")
for i in range(5):
    elemento = int(input())
    x.append(elemento)

y = []
print("Digite 5 elementos para o vetor y:")
for i in range(5):
    elemento = int(input())
    y.append(elemento)

soma = [x[i] + y[i] for i in range(5)]
print("Soma entre x e y:", soma)

produto = [x[i] * y[i] for i in range(5)]
print("Produto entre x e y:", produto)

diferenca = [elemento for elemento in x if elemento not in y]
print("Diferença entre x e y:", diferenca)

interseccao = [elemento for elemento in x if elemento in y]
print("Intersecção entre x e y:", interseccao)

uniao = x + [elemento for elemento in y if elemento not in x]
print("União entre x e y:", uniao)
