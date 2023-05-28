#q7

fitas = int(input("Digite a qt de fitas da locadora: "))
valor_aluguel = float(input("Digite o valor cobrado por cada aluguel: "))

faturamento_anual = (fitas * valor_aluguel * 12) / 3
multas_por_mes = (fitas * valor_aluguel / 10) * 0.1
fitas_no_final_do_ano = int(fitas * (1 - 0.02) + (fitas / 10))

print("Faturamento anual da locadora: R$ {:.2f}".format(faturamento_anual))
print("Valor ganho com multas por mes: R$ {:.2f}".format(multas_por_mes))
print("Quantidade de fitas no final do ano: {}".format(fitas_no_final_do_ano))
