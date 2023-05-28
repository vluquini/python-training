#q4

valorhora = int(input("Valor hora: "))
numeroauladada = int(input("Numero de aula dadas: "))
inss = 0.07
horaspordia = 8

salario_bruto = (valorhora * horaspordia) * numeroauladada
salario_liquido = salario_bruto - (salario_bruto * inss)

print(f"salarioliquido {salario_liquido}")
