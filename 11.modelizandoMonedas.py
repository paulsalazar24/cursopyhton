def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿cuantos pesos " + tipo_pesos + "  tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("tienes $" + dolares + "dòlares")

menu = """
Bienvenido al conversor de monedas😊

1 - pesos colombianos
2 - pesos mexicanos
3 - pesos argentinos

"""
opcion = input(menu)

if opcion == 1:
    conversor("pesos colombianos", 3.70)
elif opcion == 2:
   conversor("pesos mexicano", 3.46)
elif opcion == 3:
    conversor("pesos argentinos", 30.89)
else:
    print('Ingresa una opciòn correcta por favor')


