# Realizar un ejercicio de comprension de datos de todos los numeros de 4 que a la vez 
# tambien son mulriplos de 6 y de 9 hasta 5 digitos
def run():#list comprehension
    
    #square = [i(EXPRESSION) for i in range(1,1000)(SEQUENCE/LIST) if ((i%4)and (i%6) and (i%9)) == 0(CONDITION/OPTIONAL)]
    square = [i for i in range(1,1000) if ((i%4== 0)and (i%6== 0) and (i%9 ==0))]
    print(square)
    
    #Edicion y actualizacion desde el git hub
    #Impresion de datos
    for i in square:
        print(i, end=("- "))

if __name__=='__main__':
    run()
