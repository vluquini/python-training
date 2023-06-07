#q2
import math

area = float(input("Digite o tamanho da área em metros quadrados: "))
litros_tinta = area / 6 * 1.1 # inclui 10% de folga

# Quantidade e preço de latas de 18 litros
latas_tinta = math.ceil(litros_tinta / 18)
preco_latas = latas_tinta * 80

# Quantidade e preço de galões de 3,6 litros
galoes_tinta = math.ceil(litros_tinta / 3.6)
preco_galoes = galoes_tinta * 25

# Quantidade e preço de latas e galões misturados
latas_misturadas = int(litros_tinta / 18) # quantidade inteira de latas
resto_litros = litros_tinta % 18 # litros restantes para completar com galões
galoes_misturados = math.ceil(resto_litros / 3.6)
preco_misturado = latas_misturadas * 80 + galoes_misturados * 25

print("Para pintar uma área de %.2f metros quadrados," % area)

print("Você pode comprar apenas %.0f lata(s) de tinta por R$ %.2f." % (latas_tinta, preco_latas))

print("Ou você pode comprar apenas %.0f galão(ões) de tinta por R$ %.2f." % (galoes_tinta, preco_galoes))

print("Ou você pode misturar %d lata(s) e %d galão(ões), totalizando %.2f litros de tinta por R$ %.2f." % (latas_misturadas, galoes_misturados, litros_tinta, preco_misturado))
