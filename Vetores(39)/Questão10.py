notas = []

for i in range(15):
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    notas.append(nota)

media_geral = sum(notas) / len(notas)

print(f"A média geral é: {media_geral:.2f}")

