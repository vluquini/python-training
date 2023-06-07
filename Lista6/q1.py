#q1
peso = float(input("Digite o peso dos peixes em quilos: "))
limite = 50.0

if peso > limite:
    excesso = peso - limite
    multa = excesso * 4.0
    print("O peso excedeu o limite em %.2f kg" % excesso)
    print("O valor da multa é de R$ %.2f" % multa)
else:
    print("O peso está dentro do limite permitido")
