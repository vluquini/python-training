#q9
valorCompra = float(input("Digite o valor de compra do produto: "))

if valorCompra < 20.0:
    percentLucro = 0.45
else:
    percentLucro = 0.3

valorVenda = valorCompra + (valorCompra * percentLucro)

print("O valor de venda do produto é R$", valorVenda)
