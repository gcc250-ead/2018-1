num_alunos = int(input())
soma_nota = 0.0
i = 0
notas = []

# lê as notas dos alunos e adiciona na lista "notas"
while i < num_alunos:
	nota = float(input())
	soma_nota += nota # "soma_nota" é um exemplo de acumulador
	notas.append(nota)
	i += 1

media_sala = soma_nota / num_alunos
print("Média da sala: %.2f" % media_sala)

# imprime a diferença de notas dos alunos
i = 0
while i < num_alunos:	
	print("Aluno %d: %.2f" % (i + 1, notas[i] - media_sala))
	i += 1


