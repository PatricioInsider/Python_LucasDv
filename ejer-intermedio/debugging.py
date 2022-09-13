
def finish():
    print("Gracias por usar nuestro programa")

def divisor(num):
    divisors=[]
    for i in range(1,num+1):
        if num%i == 0:
            divisors.append(i)
    return divisors
    
#Manejo de debugging, entramos al panel de errores
'''Practica de list compreshions
def run (num):
    square =[i for i in range(1,num+1) if num%i==0]
    print(square)
    finish()
'''
def run():
    try:
        num = int(input("Ingresa un numero: "))
        try:
            if num <0 :
                raise ValueError("Debes ingresar un numero positivo")
            print(divisor(num))
            finish()
        except ValueError as nega:
            print(nega)

    except ValueError:
        print("Debes ingresar un numero ") 


if __name__=='__main__':
    run()