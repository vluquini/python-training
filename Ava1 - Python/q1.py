#q1
'''Desenvolver um programa que a partir da idade e peso do paciente calcule a dosagem de
determinado medicamento e escreva a receita informando quantas gotas do medicamento
o paciente deve tomar por dose. Considere que o medicamento em questão possui 500mg
por ml, e que cada ml corresponde a 20 gotas.

a. Adultos ou adolescentes desde 12 anos, inclusive, se tiverem peso igual
ou acima de 60kg devem tomar 1000mg; com peso abaixo de 60kg devem
tomar 875mg.
b. Para Crianças e adolescentes abaixo de 12 anos é dosagem calculada
pelo peso corpóreo conforme a tabela a seguir:
i. 5kg a 9 kg = 125mg;
ii. 9.1kg a 16kg = 250mg;
iii. 16.1kg a 24kg = 375mg;
iv. 24.1kg a 30kg = 500mg;
v. Acima de 30kg 750mg.'''

idade = int(input("Digite a idade do paciente: "))
peso = float(input("Digite o peso do paciente (em kg): "))

if idade >= 12:
    if peso >= 60:
        dosagem = 1000
    else:
        dosagem = 875
else:
    if peso < 5:
        print("Peso abaixo do mínimo permitido para tomar este medicamento.")
    elif peso <= 9:
        dosagem = 125
    elif peso <= 16:
        dosagem = 250
    elif peso <= 24:
        dosagem = 375
    elif peso <= 30:
        dosagem = 500
    else:
        dosagem = 750

quantidade_ml = dosagem / 500
quantidade_gotas = quantidade_ml * 20

print("Receita médica:")
print(f"Administrar {quantidade_gotas:.0f} gotas por dose, a cada 8h.")



