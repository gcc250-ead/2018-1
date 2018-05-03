"""
GCC-250 Fundamentos de Programação
2018/1
Prof Paulo Afonso e Prof. Paula Cardoso
- modularização - conta vogais em uma string
"""
def contaVogais(s):
	cont=0
	tamanho=len(s)
	pos=0
	while pos<tamanho:
		if s[pos]=="a" or s[pos]=="e" or s[pos]=="i" or s[pos]=="o" or s[pos]=="u":
			cont=cont+1
		pos=pos+1
	return cont

def principal():
	palavra=input()
	totalVogais = contaVogais(palavra)
	print(totalVogais)

principal()
