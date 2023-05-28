#q8

numero_conta = int(input("Digite o número da conta corrente: "))

inverso = int(str(numero_conta)[::-1])

soma = numero_conta + inverso

digitos = [int(digito) for digito in str(soma)]

soma_multiplicacao = sum((indice + 1) * digito for indice, digito in enumerate(digitos))

digito_verificador = soma_multiplicacao % 10

print("O dígito verificador da conta corrente {} é {}".format(numero_conta, digito_verificador))
