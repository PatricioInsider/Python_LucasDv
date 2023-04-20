def parte_decimal(num):
    for i in range(15):
        if num <= 2**i:
            if num ==2**i:
                return i
            return i-1
            

def parte_entera(numero):
    entero = int(numero)
    binario_entero = ""
    while entero>0:
        aux =parte_decimal(entero)
        print(f" {entero}\n-", 2**aux, f"Pos ({aux})")
        entero -= 2**aux
        print(entero)


def decimal_a_binario(numero):
    entero = int(numero)
    decimal = abs(numero - entero)
    binario_entero = ""
    while entero > 0:
        residuo = entero % 2
        entero = entero // 2
        binario_entero = str(residuo) + binario_entero
        
    binario_decimal = ""
    
    print("Parte decimal de BINARIO max 8")
    n = 1
    while decimal > 0 and n <= 8:  # máximo de 10 decimales
        aux= round(decimal, 3) 
        decimal = decimal * 2
        print(f"- {aux} x 2 = {round(decimal,3)}")
        if decimal >= 1:
            binario_decimal += "1"
            decimal -= 1
        else:
            binario_decimal += "0"
        n += 1
    binario = binario_entero + "." + binario_decimal
    return binario

def decimal_a_octal(numero):
    entero = int(numero)
    decimal = numero - entero
    resultado_entero = ""
    resultado_decimal = ""
    while entero > 0:
        resto = entero % 8
        entero //= 8
        resultado_entero = str(resto) + resultado_entero
        
    print("Parte decimal de OCTAL max 8")
    if decimal > 0:
        resultado_decimal = "."
    l=1
    while decimal > 0 and l<=8:
        aux= round(decimal, 3) 
        decimal *= 8
        print(f"- {aux} x 8 = {round(decimal,3)}")
        parte_entera = int(decimal)
        resultado_decimal += str(parte_entera)
        decimal -= parte_entera
        l +=1
    return resultado_entero + resultado_decimal

def decimal_a_hexadecimal(numero):
    entero = int(numero)
    decimal = numero - entero
    resultado_entero = ""
    resultado_decimal = ""
    while entero > 0:
        resto = entero % 16
        entero //= 16
        resultado_entero = hex(resto)[2:].upper() + resultado_entero
    
    print("Parte decimal de HEXADECIMAL max 8")
    if decimal > 0 :
        resultado_decimal = "."
    l=1
    while decimal > 0 and l<=8:
        aux= round(decimal, 3)
        decimal *= 16
        print(f"- {aux} x 16 = {round(decimal,3)}")
        parte_entera = int(decimal)
        resultado_decimal += hex(parte_entera)[2:].upper()
        decimal -= parte_entera
        l +=1
    return resultado_entero + resultado_decimal



def run():
    numero_decimal = float(input("Ingresa el numero"))
    
    print ("Pate entera ")
    parte_entera(numero_decimal)
    
    numero_binario = decimal_a_binario(numero_decimal)
    numero_octal = decimal_a_octal(numero_decimal)
    numero_hexadecimal = decimal_a_hexadecimal(numero_decimal)
    print(f"Binario {numero_binario}")
    print(f"Octal: {numero_octal} ")
    print(f"Hexadecimal: {numero_hexadecimal} ")
    print ("-----------------------------------------------------")


if __name__ == "__main__":
    run()
    