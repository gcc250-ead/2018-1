def lerDadosAluno():
	nome = input("Informe o nome do aluno: ")
	nota = float(input("Informe a nota do aluno: "))
	return nome, nota

def imprimeLinha():
	print("------------------------------")

def principal():
	nome, nota = lerDadosAluno()

	print("\nRelatório de alunos")
	imprimeLinha()
	print("Nome		Nota")
	imprimeLinha()
	print("%s		%.2f"%(nome, nota))
	
principal()
