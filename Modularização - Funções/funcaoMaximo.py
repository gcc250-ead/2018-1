"""
GCC-250 Fundamentos de Programação
2018/1
Prof Paulo Afonso e Prof. Paula Cardoso
- Modularização: Escreva uma função chamada Maximo, que recebe dois
 números reais e retorna o maior deles. Escreva um programa para 
 utilizar esta função, exibindo no dispositivo de saída padrão 
 o resultado obtido pela função. Se os dois valores forem iguais, 
 apenas exiba um deles.
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
