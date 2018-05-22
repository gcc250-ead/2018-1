"""
GCC-250 Fundamentos de Programação
2018/1
Prof Paulo Afonso e Prof. Paula Cardoso
- Exemplos com modularização e repeticao
Escreva um programa que tem uma função que 
recebe um número inteiro e mostre na tela 
os seus divisores, e também retorne:
O seu segundo menor divisor
O seu segundo maior divisor
"""
def QuadDif(a,b):
	n=(a-b)*(a-b)
	print(n)
def QuadSoma(a,b):
	n=(a+b)*(a+b)
	print(n)
def SomaQuad(a,b):
	return (a*a)+(b*b)
def DifQuad(a,b):
	return (a*a)-(b*b)
def principal():
	a,b = map(int, input().split())
	tipo=int(input())
	
	if tipo==1:
		QuadDif(a,b)
	elif tipo==2:
		QuadSoma(a,b)
	elif tipo==3:
		total=SomaQuad(a,b)
		print(total)
	elif tipo==4:
		total=DifQuad(a,b)
		print(total)
principal()
