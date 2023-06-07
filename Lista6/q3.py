#q3

tipo_carne = input("Digite o tipo de carne desejado: ")
quantidade = float(input("Digite a quantidade desejada (em Kg): "))
pagamento = input("Deseja pagar com o cartão Tabajara? (sim ou não): ")

preco_total = 0.0

if tipo_carne == "File Duplo":
    if quantidade <= 5:
        preco_total = quantidade * 4.9
    else:
        preco_total = quantidade * 5.8
elif tipo_carne == "Alcatra":
    if quantidade <= 5:
        preco_total = quantidade * 5.9
    else:
        preco_total = quantidade * 6.8
elif tipo_carne == "Picanha":
    if quantidade <= 5:
        preco_total = quantidade * 6.9
    else:
        preco_total = quantidade * 7.8

if pagamento == "sim":
    desconto = (preco_total * 0.05)
    preco_final = preco_total - desconto
    tipo_pagamento = "Cartão Tabajara"
else:
    desconto = 0.0
    preco_final = preco_total
    tipo_pagamento = "Outro cartão ou dinheiro"

print("\nCupom Fiscal:")
print("Tipo de carne: %s" % tipo_carne)
print("Quantidade: %.2f Kg" % quantidade)
print("Preço total: R$ %.2f" % preco_total)
print("Tipo de pagamento: %s" % tipo_pagamento)
print("Valor do desconto: R$ %.2f" % desconto)
print("Valor a pagar: R$ %.2f" % preco_final)
