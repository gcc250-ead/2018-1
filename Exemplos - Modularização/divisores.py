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

def divisores (n):
        i=1
     
        menor=n
        while i<=n:
                if n%i ==0:
                        print(i, end=" ")
                        if i!=n:
                                maior=i
                        if i<menor and i!=1:
                                menor=i
                i=i+1
        
        return menor,maior

def principal():
	n=int(input())
	segundoMenor, segundoMaior=divisores(n)
	print()
	print (segundoMenor, segundoMaior)

principal()
