# Calcula e imprime o imposto a ser pago e a forma de pagamento
salario = float(input())
if (salario > 1000):
	imposto = (salario * 5) / 100
	if (imposto < 100):
		print("Imposto = R$ %.2f - Pagamento à vista" % imposto);
	else:
		print("Imposto = R$ %.2f - Pagamento parcelado" % imposto);
else:
	print("Não precisa pagar imposto! :)")
