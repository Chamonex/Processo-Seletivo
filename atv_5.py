# OBS:
# a string será obtida pelo teclado do usuário!

def inverter(str):
    # metodo alterando cada caractere manualmente:

    str_invertida = ""
    for i in range(len(str) -1, -1, -1):
        str_invertida += str[i]
    return str_invertida


str = input("qual string deseja inverter? ")
print(inverter(str))
