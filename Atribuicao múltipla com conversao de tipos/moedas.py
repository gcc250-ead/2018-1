"""
GCC-250 Fundamentos de Programação
2018/1
Prof Paulo Afonso e Prof. Paula Cardoso
- Moedas
"""
dez, cinco = map(int,input().split())
total = dez*10 + cinco*5
um=total//200
resto=total%200
print(um,resto)

