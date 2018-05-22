"""
GCC-250 Fundamentos de Programação
2018/1
Prof Paulo Afonso e Prof. Paula Cardoso
- Exemplos com modularização e repeticao
Faça uma função que receba dois números positivos 
e calcula a soma de n números inteiros existentes 
entre eles, inclusive estes números.
"""

def soma (n1,n2):
    soma=0
    v=n1
    while v<=n2:
        soma=soma+v
        v=v+1
    return soma
def principal():
    n1,n2=map(int,input().split())
    print(soma(n1,n2))
principal()
