# Ejercicios de Funciones integradas de un programa
def polindromo(palabra):
    palabra = (palabra.lower()).replace(' ', '')
    palVolteada = palabra[::-1]
    if palabra == palVolteada:
        return True
    else:
        return False


def run():

    verdadero = 'La palabra es polindromo'
    falso = 'La palabra no es polindromo'

    palabra = str(input('Ingresa la palabra a evaluar: '))
    comprobacion = polindromo(palabra)
    if comprobacion == True :
        return print(verdadero)
    else:
        return print(falso)


#Comienzo del programa siempre se ocupa esta linea
if __name__ == '__main__':
#     for i in range(4):
#         run()
# print('Finalizo')

    x = 1
    while x <= 4:
        run()
        x += 1
#si definimos las variables en MAYUSCULAS es constante