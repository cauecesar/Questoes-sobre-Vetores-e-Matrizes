notas = [
    [7, 8, 9],
    [5, 6, 4],
    [8, 9, 7],
]

pior_nota_prova_1 = pior_nota_prova_2 = pior_nota_prova_3 = 0

for aluno_notas in notas:
    pior_nota = min(aluno_notas)
    indice_pior_nota = aluno_notas.index(pior_nota)

    if indice_pior_nota == 0:
        pior_nota_prova_1 += 1
    elif indice_pior_nota == 1:
        pior_nota_prova_2 += 1
    else:
        pior_nota_prova_3 += 1

print(f"Número de alunos cuja pior nota foi na prova 1: {pior_nota_prova_1}")
print(f"Número de alunos cuja pior nota foi na prova 2: {pior_nota_prova_2}")
print(f"Número de alunos cuja pior nota foi na prova 3: {pior_nota_prova_3}")
