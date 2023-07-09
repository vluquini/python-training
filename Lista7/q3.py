#q3
def fahrenheit_para_celsius(temp_f):
    temp_c = (temp_f - 32) * 5/9
    return temp_c

temp_f = int(input("Digite um numero: "))

temp_c = fahrenheit_para_celsius(temp_f)

print(f"{temp_f} graus Fahrenheit são equivalentes a {temp_c:.2f} graus Celsius")



