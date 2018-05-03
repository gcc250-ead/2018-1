"""
GCC-250 Fundamentos de Programação
2018/1
Prof Paulo Afonso e Prof. Paula Cardoso
- Funcao: maior de dois numeros
"""

def Maximo (a,b):
	if a>=b:
		return a
	else:
		return b

def principal() :
	n1, n2 = map (int,input().split())
	print(Maximo(n1,n2))
	
principal()
