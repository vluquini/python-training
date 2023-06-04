#q15
salario_bruto = float(input("Digite o salário bruto do funcionário: "))
valor_prestacao = float(input("Digite o valor da prestação desejada: "))

limite_prestacao = salario_bruto * 0.3

if valor_prestacao <= limite_prestacao:
    print("Empréstimo concedido.")
else:
    print("Empréstimo não concedido.")
