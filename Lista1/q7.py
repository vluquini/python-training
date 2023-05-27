#q7
angulo = 80
radianos = angulo * 3.14159 / 180.0
seno = (radianos - (radianos ** 3) / 6 + (radianos ** 5) / 120 - (radianos ** 7) / 5040)
cosseno = (1 - (radianos**2) / 2 + (radianos ** 4) / 24 - (radianos ** 6) / 720)
tangente = (radianos + (radianos ** 3) / 3 + (2 * radianos ** 5) / 15 + (17 * radianos ** 7) / 315)
secante = (1 / cosseno)
cosecante = (1 / seno)
cotangente = (1 / tangente)
print("Seno: ", seno)
print("Cosseno: ", cosseno)
print("Tangente: ", tangente)
print("Secante: ", secante)
print("Cosecante: ", cosecante)
print("Cotangente: ", cotangente)