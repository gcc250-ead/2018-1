# Imprime a situação do aluno com base na sua nota final
nota_final = float(input())
if (nota_final >= 60):
	print("Aprovado :)");
elif (nota_final >= 50):
	print("Em recuperação :|");
else:
	print("Reprovado :(")
