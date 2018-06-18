aluno = {}
aluno["Nome"] = input()
aluno["Notas"] = list(map(float, input().split()))

soma = 0.0
qtde_notas = len(aluno["Notas"])

for n in aluno["Notas"]:
	soma += n

media = soma / qtde_notas

print(aluno["Nome"])
print(media)
if media >= 60:
	print("Aprovado")
else:
	print("Reprovado")
