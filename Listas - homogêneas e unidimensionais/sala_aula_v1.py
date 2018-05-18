nota_aluno1 = float(input())
nota_aluno2 = float(input())
nota_aluno3 = float(input())

media_sala = (nota_aluno1 + nota_aluno2 + nota_aluno3) / 3

print("Média da sala: %.2f" % media_sala)
print("Aluno 1: %.2f" % (nota_aluno1 - media_sala))
print("Aluno 2: %.2f" % (nota_aluno2 - media_sala))
print("Aluno 3: %.2f" % (nota_aluno3 - media_sala))
