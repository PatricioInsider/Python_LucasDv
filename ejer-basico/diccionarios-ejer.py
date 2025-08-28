#Diccionarios

def run():
    mi_diccionario = {
        'llave1' : 1,#PAra diccionarios te retorna un valor con la palabra clave {palabraclae:retorno}
        'llave2' : 2,
        'llave3' : 3,
    }
"""  print(mi_diccionario['llave2']) """


def poblacion():
    paises = {
        'Ecuador': 246783,
        'Argentina': 346783,
        'Colombia': 446783,
        'VEnezuela': 5437777,
    }

    for pais in paises.keys(): #Se extrae la llave del diccionario metodo [diccionario.keys()]
        print(pais)

    for llave in paises.values(): #Se extrae los valores del diccionario metodo [diccionario.values()]
        print(llave)

    for llave, valor in paises.items(): #Se extrae las llaves y los valores, por ende se necesita 2 variables  del diccionario metodo [diccionario.items()]
        print(llave, 'Tiene personas: ', valor)


    for i in paises:
        clave = paises[str(i)]
        print(i, clave)




if __name__ == '__main__':
    run()
    poblacion()