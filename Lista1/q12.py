#q12
volumePote = 15 * 10 * 13
raio = 1.2
pi = 3.14
volume_bolinha = (4/3 * pi) * (raio**3)
fatorEmpacotamento = 0.74
numBolinhas = int(volumePote * fatorEmpacotamento / volume_bolinha)
print("Cabem aproximadamente: ", numBolinhas, " bolinhas.")