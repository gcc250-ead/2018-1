invest_inicial = float(input())
tx_rend = float(input())
mes = 1 # isso é um contador
acumulado = invest_inicial # isso é um acumulador
while mes <= 12:
	acumulado = acumulado + (acumulado * tx_rend)
	print(acumulado)
	mes = mes + 1
