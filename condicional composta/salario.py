"""
GCC-250 Fundamentos de Programação
2018/1
Prof Paulo Afonso e Prof. Paula Cardoso
- Estrutura condicional composta: empresa
Uma empresa concedeu um bônus de 20% do valor do salário a todos os funcionários
com tempo de trabalho na empresa igual ou superior a 5 anos e um bônus de 10% aos demais.
Calcule e exiba o valor
"""

bonus=0

salario=float(input())
tempo=int(input())

if tempo>=5:
	bonus=salario*0.20
else:
	bonus=salario*0.10

print("O valor do bônus é ",bonus)
