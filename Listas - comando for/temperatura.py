"""
GCC-250 Fundamentos de Programação
2018/1
Prof Paulo Afonso e Prof. Paula Cardoso
Listas: Faça um subprograma que leia as temperaturas registradas, 
diariamente, durante uma semana. Além disso, faça um subprograma 
que determina em quantos dias dessa semana a temperatura esteve 
acima da média.
"""

def calculaMedia(t):
    soma=0
    for i in range(len(t)):
        soma=soma+t[i]
    return soma/len(t)

def acimaMedia(t):
	media = calculaMedia(t)
	dias=0
	for i in range (len(t)):
		if t[i]>media:
			dias = dias +1
	return dias
	
def principal():
    tempo=[]
    for i in range (7):
        t=float(input())
        tempo.append(t)
    print(acimaMedia(t))
        
principal()
