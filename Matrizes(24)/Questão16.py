gabarito = ['a', 'b', 'c', 'd', 'e', 'e', 'd', 'c', 'b', 'a']


alunos = [
    {'matricula': 123, 'respostas': ['a', 'b', 'c', 'd', 'e', 'e', 'd', 'c', 'b', 'a']},
    {'matricula': 456, 'respostas': ['e', 'd', 'c', 'b', 'a', 'a', 'b', 'c', 'd', 'e']},
    {'matricula': 789, 'respostas': ['a', 'b', 'c', 'd', 'e', 'e', 'd', 'c', 'b', 'a']}
]

for aluno in alunos:
    aluno['nota'] = sum(1 for i in range(10) if aluno['respostas'][i] == gabarito[i])

aprovados = sum(1 for aluno in alunos if aluno['nota'] >= 7)
percentual_aprovacao = (aprovados / len(alunos)) * 100

for aluno in alunos:
    print(f"Matrícula: {aluno['matricula']}, Respostas: {aluno['respostas']}, Nota: {aluno['nota']}")

print(f"Percentual de aprovação: {percentual_aprovacao}%")

