'''
Escribe un programa que pregunte al usuario su nombre, edad y teléfono y lo guarde en un diccionario.
Después, debe mostrar por pantalla el mensaje ‘{nombre} tiene {edad} años y su número de teléfono es
{teléfono}
'''
def datos():
    dato = {"nombre":str(input("Ingresa tu nombre: ")),
            "edad":str(input("Ingresa edad: ")),
            "telefono":str(input("Ingresa numero de telefono: "))}
    #Escritura del programa
    
    print(dato["nombre"]," tiene ", dato["edad"], " y su numero de telefono es ", dato["telefono"]) 
    
    pass

if __name__=='__main__':
    datos()