"""
GCC-250 Fundamentos de Programação
2018/1
Prof Paulo Afonso e Prof. Paula Cardoso
- cálculo de fatorial
"""

n = int (input())
fat = 1
c = 1
while c <= n:
	fat = fat * c
	c = c + 1
print(n," != ",fat)
