#q5

km_por_litro = 12
distancia_percorrida = float(input("Digite a distancia percorrida em km: "))
tempo_gasto = float(input("Digite o tempo gasto em horas: "))
velocidade_media = distancia_percorrida / tempo_gasto
litros_gastos = distancia_percorrida / km_por_litro

print("Velocidade média: {:.2f} km/h".format(velocidade_media))
print("Tempo gasto: {:.2f} horas".format(tempo_gasto))
print("Distância percorrida: {:.2f} km".format(distancia_percorrida))
print("Quantidade de litros gastos: {:.2f} litros".format(litros_gastos))
