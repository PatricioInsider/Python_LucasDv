# COMPAÑIA MULTINACIONAL RAPPI

print("COMPAÑIA MULTINACIONAL RAPPI\n")

print("Bienvenido, al sistema de asignacion de vacaciones RAPPI")

nombre_empleado = str(input("Nombre del empleado"))
antiguedad_empleado = int(input("Años de servicio\n (ejemplo:1, 2, 3, etc)\n "))
clasif_departamento = str(input("Ingresa el departamento\n (ejemplo: Departamento de atencion al cliente, Departamento de logistica, Gerencia)\n  "))
clave_departamento = str(input("Ingresa la clave del departamento\n "))
clasif_departamento = clasif_departamento.lower()

print("DATOS")
print(nombre_empleado, (" y "), antiguedad_empleado, (" años de servicio"))

if clave_departamento == ("1") and clasif_departamento == ("departamento de atencion al cliente") :
    print("RESULTADO")
    
    if antiguedad_empleado == 1 and clasif_departamento == ("departamento de atencion al cliente") :
        print(nombre_empleado + (", obtiene 6 dias de vacaciones"))
        
    elif antiguedad_empleado >= 2 and antiguedad_empleado <= 6 and  clasif_departamento == ("departamento de atencion al cliente") :
        print(nombre_empleado + (" , obtiene 14 dias de vacaciones"))  
    
    elif antiguedad_empleado <= 7 and clasif_departamento == ("departamento de atencion al cliente"):
        print(nombre_empleado + (" , obtiene 20 dias de vacaciones"))
        

elif clave_departamento == ("2") and clasif_departamento == ("departamento de logistica") :
    print("RESULTADO")
    
    if antiguedad_empleado == 1 and clasif_departamento("departamento de logistica") :
        print(nombre_empleado + (", obtiene 7 dias de vacaciones"))
        
    elif antiguedad_empleado >= 2 and antiguedad_empleado <= 6 and clasif_departamento == ("departamento de logistica") :
        print(nombre_empleado + (" , obtiene 15 dias de vacaciones"))  
    
    elif antiguedad_empleado <= 7 and clasif_departamento == ("departamento de logistica"):
        print(nombre_empleado + (" , obtiene 22 dias de vacaciones"))

        
    
elif clave_departamento == ("3") and clasif_departamento == ("gerencia") :
    print("RESULTADO")
    
    if antiguedad_empleado == 1 and clasif_departamento == ("gerencia") :
        print(nombre_empleado + (", obtiene 10 dias de vacaciones"))
        
    elif antiguedad_empleado >= 2 and antiguedad_empleado <= 6 and clasif_departamento == ("gerencia") :
        print(nombre_empleado + (" , obtiene 20 dias de vacaciones"))  
    
    elif antiguedad_empleado <= 7 and clasif_departamento == ("gerencia"):
        print(nombre_empleado + (" , obtiene 30 dias de vacaciones"))

else :
    print("Departamento o clave invalidos, intentelo de nuevo\n ")

print("Gracias por utilizar el sistema de asignacion de vacaciones RAPPI")

