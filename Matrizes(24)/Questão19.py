
alunos = [

]

for aluno in alunos:
    aluno[3] = aluno[1] + aluno[2]  

aluno_maior_nota = max(alunos, key=lambda x: x[3])
print(f"Matrícula com maior nota final: {aluno_maior_nota[0]}")

media_notas_finais = sum(aluno[3] for aluno in alunos) / len(alunos)
print(f"Média aritmética das notas finais: {media_notas_finais}")

