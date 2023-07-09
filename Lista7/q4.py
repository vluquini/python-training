#q4
def fahrenheit_para_celsius(temp_f):
    temp_c = (temp_f - 32) * 5/9
    return temp_c

for temp_c in range(101):
    temp_f = (temp_c * 9/5) + 32
    print(f"{temp_c} graus Celsius = {temp_f:.1f} graus Fahrenheit")
