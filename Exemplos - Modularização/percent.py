"""
GCC-250 Fundamentos de Programação
2018/1
Prof Paulo Afonso e Prof. Paula Cardoso
- Exemplos com modularização e repeticao
Escreva uma função que receba como parâmetro 
uma string e um caractere, e retorne o 
percentual que indica a quantidade de 
ocorrências desse caractere com relação ao
total de caracteres válidos.
"""
def conta (palavra, letra):
    c=0
    tam=len(palavra)
    i=0
    validos=0
    while i<tam:
        if palavra[i]!=" ":
            validos=validos+1
            if palavra[i]==letra:
                c=c+1
        i=i+1
    por=c/validos
    return por

def principal():
    p=input()
    letra=input()
    n=conta(p,letra)
    print(n)
principal()
    
