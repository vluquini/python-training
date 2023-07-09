#q1
'''
Criar um programa que leia o preço de compra e o preço de venda de 100
produtos. o programa devera imprimir quantas mercadoria proporcionam a)
lucro < 10%, b) 10% <= lucro <= 20%, c) lucro > 20%.'''

num_produtos = 5

produtos_lucro_menor_10 = 0
produtos_lucro_entre_10_e_20 = 0
produtos_lucro_maior_20 = 0

for i in range(num_produtos):
    preco_compra = float(input(f"Digite o preço de compra do produto {i + 1}: "))
    preco_venda = float(input(f"Digite o preço de venda do produto {i + 1}: "))

    lucro = (preco_venda - preco_compra) / preco_compra * 100

    if lucro < 10:
        produtos_lucro_menor_10 += 1
    elif lucro <= 20:
        produtos_lucro_entre_10_e_20 += 1
    else:
        produtos_lucro_maior_20 += 1

print(f"Número de produtos com lucro menor que 10%: {produtos_lucro_menor_10}")
print(f"Número de produtos com lucro entre 10% e 20%: {produtos_lucro_entre_10_e_20}")
print(f"Número de produtos com lucro maior que 20%: {produtos_lucro_maior_20}")
