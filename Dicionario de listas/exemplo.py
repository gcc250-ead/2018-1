aluno = {"Nome": "José das Couves", 
		 "Matricula": 77777777, 
		 "Notas": [100, 93.5, 82.6, 71.2]}
# acessa a primeira nota do aluno
print(aluno["Notas"][0])
# imprime a quantidade de notas do aluno
print(len(aluno["Notas"]))
# adiciona uma nova nota na lista de notas do aluno
aluno["Notas"].append(60)
# imprime a quantidade de notas do aluno
print(len(aluno["Notas"]))
