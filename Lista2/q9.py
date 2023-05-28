#q9

frase = input("Digite uma frase: ")

palavras = frase.split()

palavras_invertidas = palavras

frase_invertida = " ".join(palavras_invertidas)

frase_invertida = frase_invertida[::-1]

print(frase_invertida)


