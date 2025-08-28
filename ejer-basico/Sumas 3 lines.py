#Condiciones WHILE suma en 3 lineas
"""x=str(input("Name"))
age=int(input("age"))
year=int(input("year"))
g=1
while g<=10 :
    print(x,"edad",age )
    age+=2
    year+=2
    g+=1
print("ya imprimimos 10 veces")
"""
"""#susesion de figonalli
num_one, num_dos=0,1 #tambien valio  """"num_one=0; num_dos=1""""
print(num_one,num_dos, end=(" "))
while num_dos <= 1600 and num_one <= 1600:
    num_one=(num_one+num_dos)
    print(num_one, end=(" "))
    num_dos=(num_one+num_dos)
    print(num_dos, end=(" "))
"""
#BREAK AND continue
user=str(input("User"))
while user == ("Pato"):
    print("Bienvenido,Asegurate de ingresar los datos correctos!! ", user)
    password=str(input("Ingresa la contraseña"))
    if password==("patricio123"):
        print("Ahora lo has logrado, gracias al esfuero")
        continue
    
print("Hola",user,("lo sentimos no reunes los requisitos"))
print("Hola mi friens)")
