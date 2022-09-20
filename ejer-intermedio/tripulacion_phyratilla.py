'''
¡Ayuda a Pyratilla a crear un diccionario llamado info_pyrates que contenga para cada miembro de la tripulación de los Pyrates un diccionario con la edad (age) y la ocupación (occupation) de cada uno.
Ayuda a Pyratilla a mostrar los datos de cada uno de los miembros de su tripulación como se muestra a continuación:
'''

def run():
    datosPyratilla = {"age":17,"ocupation":"Capitan del barco"}
    datosPyerce= {"age":16,"ocupation":"navegante del barco"}
    datosPym = {"age":16,"ocupation":"timonel"}
    datosPyo = {"age":1.5,"ocupation":"loro del barco"}
    
    
    info_pyratilla= { "Pyratilla":datosPyratilla,
                     "Pyerce":datosPyerce,
                     "Pym":datosPym,
                     "Pyo":datosPyo}
    for key,val in info_pyratilla.items():
        print("{} tiene {} y es el {}".format(key,val["age"],val["ocupation"]))
       
    '''
    for name in info_pyratilla.items():
        for i in name.items():
            print("El pirata {} tiene {} y es {}".format(i))
    '''
    
        

if __name__=='__main__':
    run()