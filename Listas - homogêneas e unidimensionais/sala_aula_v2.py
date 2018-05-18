num_alunos = int(input()) # lê a quantidade de alunos da sala
soma_nota = 0.0 # "soma_nota" é um exemplo de acumulador
i = 0 # "i" é um exemplo de contador
notas = [] # "notas" é uma lista vazia

# lê a nota do aluno e a adiciona na lista "notas"
while i < num_alunos:
	nota = float(input())
	soma_nota += nota 
	notas.append(nota)
	i += 1

media_sala = soma_nota / num_alunos
print("Média da sala: %.2f" % media_sala)

# imprime a diferença de notas dos alunos
i = 0 # é importante inicializar o contador aqui
while i < num_alunos:	
	print("Aluno %d: %.2f" % (i + 1, notas[i] - media_sala))
	i += 1

