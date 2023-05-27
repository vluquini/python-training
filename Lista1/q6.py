#q6
segundo = 1
minutos = segundo * 60
horas = 60 * minutos
total = ((3 * horas) + (27 * minutos) + (17 * segundo))
distanciaKM = 65
metrosSegundos = (distanciaKM * 1000) / total
print("Velocidade em m/s: ", metrosSegundos)