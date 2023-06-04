#q10
nome_municipio = input("Digite o nome do município: ")
quantidade_eleitores = int(input("Digite a quantidade de eleitores aptos: "))
numero_votos_primeiro_colocado = int(input("Digite o número de votos do candidato mais votado: "))

if quantidade_eleitores > 20000 and numero_votos_primeiro_colocado / quantidade_eleitores <= 0.5:
    print("O município de", nome_municipio, "terá segundo turno.")
else:
    print("O município de", nome_municipio, "não terá segundo turno.")

