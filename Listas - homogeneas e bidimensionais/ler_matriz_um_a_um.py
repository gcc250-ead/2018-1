mat = []
nLinhas = 2
nColunas = 3

for i in range(nLinhas):
	linha = []
	for j in range(nColunas):
		elemento = int(input())
		linha.append(elemento)
	mat.append(linha)

print(mat)
