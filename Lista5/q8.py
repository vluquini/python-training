#q8
nome = input("Escreva o nome do aluno: ")
nota1 = float(input("Escreva a primeira nota: "))
nota2 = float(input("Escreva a segunda nota: "))

media = (nota1 + nota2) / 2

print("Nome: ", nome)
print("Nota 1: ", nota1)
print("Nota 2: ", nota2)
print("Media: ", media)

if media >= 7.0:
    print("Voce foi aprovado.")
elif media < 3.0:
    print("Voce foi reprovado.")
else:
    print("Voce esta na prova final.")
