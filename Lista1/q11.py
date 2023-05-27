#q11
valorCerveja = 2.2
valorMacarrao = 8.73
valorMolho = 3.45
valorCebola = 5.4
valorAlho = 30
valorPao = 25
valorTotal = ((75 * valorCerveja) + (2 * valorMacarrao) +  valorMolho + (valorCebola / 1000)
            * 420 + valorAlho / 1000 * 250 + valorPao / 1000 * 450)
print("Valor total: ", valorTotal)
print("Valor individual: ", valorTotal/5)
