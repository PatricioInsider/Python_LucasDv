# PROCESO DE DESARROLLO DEL FORMULARIO DE PYRATILLA 
print('Formulario de Pyratilla de su tripulacion')
name = str(input('Nombre :  '))
age = int(input('Edad   :  '))
hobby = str (input('Breve descripcion de tu Hobby  :  '))
dream = str(input('Cual es tu sueño :  '))

#Reemplazo de cadenas dentro de un print
if name.istitle() and age >= 16 and age <= 40: #Cumple las 2 condiciones edad y nombre
    if len(hobby) >= 10:
        if not dream.isspace(): 
            print('Correcto ya estas inscrito en la tripulacion')

        else:
            print('Lo lamento {} no cumples con las caracteriticas'.format(name), 'revisa los datos ingresados')
    else:
        print('Lo lamento {} no cumples con las caracteriticas'.format(name), 'revisa los datos ingresados')
else:
    print('Lo lamento {} no cumples con las caracteriticas'.format(name), 'revisa los datos ingresados')

# Datos Booleanos
condicionName = False
condicionAge = False
condicionHobby = False
condicionDream = False
# Se da por entendido que las condiciones comienzan siendo falsas y luego cambian a true

name = 'Mario'
age = 16
hobby = 'Ba;ar perros'
dream = 'Trabajar desde casa'
# Evaluamos cada una de las condiciones
# Si el nombre se encuentra en mayusculas es true

if name.istitle():
    condicionName = True
else:
    print('Como estas 2')

print(condicionName)