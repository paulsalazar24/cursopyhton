def run():
    mi_diccionario = {
        'llave1' : 1,
        'llave2' : 2,
        'llave3' : 3,

    }

    # print(mi_diccionario['llave1'])
    # print(mi_diccionario['llave2'])
    # print(mi_diccionario['llave3'])

poblacion_paises = {
    'Argentina': 34567,
    'Perù' : 2345,
    'Bolivia' : 63543,
}

# regresa las llaves con el metodo keys
# for pais in poblacion_paises.keys():
#     print(pais)


# regresa los valores del diccionario con el metodo values
# for pais in poblacion_paises.values():
#     print(pais)


# regresa las llaves y valores con el metodo items
for pais, poblacion in poblacion_paises.items():
    print(pais + ' tiene ' + str(poblacion) + ' habitantes')




if __name__ == '__main__':
    run()


