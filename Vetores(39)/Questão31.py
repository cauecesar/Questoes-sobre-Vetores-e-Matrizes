
vetor1 = []
print("Digite 10 elementos para o primeiro vetor:")
for i in range(10):
    elemento = int(input())
    vetor1.append(elemento)

vetor2 = []
print("Digite 10 elementos para o segundo vetor:")
for i in range(10):
    elemento = int(input())
    vetor2.append(elemento)

uniao = set(vetor1 + vetor2)

uniao_lista = list(uniao)
print("A união dos dois vetores é:", uniao_lista)

