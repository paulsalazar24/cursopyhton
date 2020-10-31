import random

def generar_password():
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f']
    simbolos = ['!', '$', '%', '&', '/', '¿', ')' '(']
    numeros = ['1', '2', '3', '4', '5', '6', '7' '8']
    
    caracteres = mayusculas + minusculas + simbolos + numeros

    password = []

    for i in range(15):
        caracter_random = random.choice(caracteres)
        password.append(caracter_random)

    password = "".join(password)
    return password


def run():
    password = generar_password()
    print('Tu nuevo password es: ' + password)




if __name__ == "__main__":
    run()