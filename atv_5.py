# OBS:
# a string será obtida pelo teclado do usuário!


def metodo_1(str):
    # metodo mais simples, utilizando 
    return str[::-1]

def metodo_2(str):
    # metodo alterando cada caractere manualmente:

    str_invertida = ""
    for i in range(len(str) -1, -1, -1):
        str_invertida += str[i]
    return str_invertida


str = input("qual string deseja inverter? ")
print("utilizando metodo 1 (implementacao simples):\n")
print(metodo_1(str))
print("utilizando metodo 2 (implementação manual):\n")
print(metodo_2(str))