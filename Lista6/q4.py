#q4
litros = float(input("Digite o número de litros vendidos: "))
tipo_combustivel = input("Digite o tipo de combustível (A-álcool ou G-gasolina): ").upper()

if tipo_combustivel == "A":
    preco_litro = 1.9

    if litros <= 20:
        desconto = 0.03
    else:
        desconto = 0.05
else:
    preco_litro = 2.5

    if litros <= 20:
        desconto = 0.04
    else:
        desconto = 0.06

preco_total = litros * preco_litro * (1 - desconto)

print("Valor a ser pago pelo cliente: R$ %.2f" % preco_total)