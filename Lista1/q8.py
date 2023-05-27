#q8
num = 123
unidade = num % 10
dezena = (num % 100) // 10
centena = num // 100
invertido = unidade * 100 + dezena * 10 + centena
print("Invertido:", invertido)