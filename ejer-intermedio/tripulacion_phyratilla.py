'''
¡Ayuda a Pyratilla a crear un diccionario llamado info_pyrates que contenga para cada miembro de la tripulación de los Pyrates un diccionario con la edad (age) y la ocupación (occupation) de cada uno.
Ayuda a Pyratilla a mostrar los datos de cada uno de los miembros de su tripulación como se muestra a continuación:
'''

def run():
    datosPyratilla = {"age":17,"ocupation":"Capitan"}
    datosPyerce= {"age":16,"ocupation":"navegante"}
    datosPym = {"age":16,"ocupation":"timonel"}
    datosPyo = {"age":1.5,"ocupation":"loro"}
    
    
    info_pyratilla= { "Pyratilla":datosPyratilla,
                     "Pyerce":datosPyerce,
                     "Pym":datosPym,
                     "Pyo":datosPyo}
    for key,val in info_pyratilla.items():
        print("{} tiene {} y es el {}".format(key,val["age"],val["ocupation"])) #otra forma de acceder a ese valor es conociendolo como matriz, asi ocupariamos info_pyratilla [key]["age"]
       
if __name__=='__main__':
    run()