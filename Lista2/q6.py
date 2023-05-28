#q6

emprestimo = float(input("Digite o valor do empréstimo: "))
juros = float(input("Digite a taxa de juros (em %): ")) / 100
meses = int(input("Digite a quantidade de meses do empréstimo: "))

prestacao = emprestimo * ((1 + juros) ** meses * juros) / ((1 + juros) ** meses - 1)

print("Valor da prestacao: R$ {:.2f}".format(prestacao))
