"""
GCC-250 Fundamentos de Programação
2018/1
Prof Paulo Afonso e Prof. Paula Cardoso
- funcao split e funcao map: exemplo
"""

x,y,z=map(float,input("Digite três numeros ").split())
print(x,y,z)
total=(x+y+z) / 3
print(total)
