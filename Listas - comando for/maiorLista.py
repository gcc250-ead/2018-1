"""
GCC-250 Fundamentos de Programação
2018/1
Prof Paulo Afonso e Prof. Paula Cardoso
- Lista: achar o maior elemento de uma lista
- Os elementos de entrada devem ser fornecidos na mesma linha e separados por espaço
"""

def achaMaior(lista):
    maior=lista[0]
    for i in range (1,len(lista)):
        if lista[i] > maior:
            maior=lista[i]         
    
    for i in range (1,len(lista)):
	    lista[i]=lista[i]+maior
    return maior


def principal ():
    preco = list (map (float, input().split()))
    print(achaMaior(preco))
    print(preco)
principal()
