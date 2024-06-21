alunos = []

print("Digite o número e a altura de 10 alunos:")
for _ in range(10):
    numero = int(input("Número do aluno: "))
    altura = float(input("Altura do aluno (em metros): "))
    alunos.append((numero, altura))


mais_alto = mais_baixo = alunos[0]

for aluno in alunos:
    if aluno[1] > mais_alto[1]:
        mais_alto = aluno
    elif aluno[1] < mais_baixo[1]:
        mais_baixo = aluno

print(f"Aluno mais alto: Número {mais_alto[0]}, Altura {mais_alto[1]}m")
print(f"Aluno mais baixo: Número {mais_baixo[0]}, Altura {mais_baixo[1]}m")
