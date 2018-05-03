"""
GCC-250 Fundamentos de Programação
2018/1
Prof Paulo Afonso e Prof. Paula Cardoso
- Modularização: Escreva um programa que tem uma função que receba 
um número inteiro e retorne seu antecessor e sucessor. Por exemplo,
 para o número 2 a função deve retornar 1 e 3. O módulo principal 
 deve chamar a função e imprimir o antecessor, o numero passado e 
 o sucessor.
"""

def Vizinho (n):
    a=n-1
    b=n+1
    return a,b
   
def principal():
    a=int(input())
    x,y=Vizinho(a)
    print(x,a,y)
principal()
