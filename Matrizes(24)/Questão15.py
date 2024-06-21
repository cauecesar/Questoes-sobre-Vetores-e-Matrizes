respostas_alunos = [
    ['a', 'b', 'c', 'd', 'a', 'b', 'c', 'd', 'a', 'b'],
    ['b', 'c', 'd', 'a', 'b', 'c', 'd', 'a', 'b', 'c'],
    ['c', 'd', 'a', 'b', 'c', 'd', 'a', 'b', 'c', 'd'],
    ['d', 'a', 'b', 'c', 'd', 'a', 'b', 'c', 'd', 'a'],
    ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']
]

gabarito = ['a', 'b', 'c', 'd', 'a', 'b', 'c', 'd','a','b']

resultado = []

for aluno in respostas_alunos:
    pontuacao = sum(1 for i in range(10) if aluno[i] == gabarito[i])
    resultado.append(pontuacao)

print("Pontuação dos alunos:", resultado)

