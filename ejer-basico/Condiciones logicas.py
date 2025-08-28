"""nombre = input("Cual es tu nombre?")
edad = str(input("Cual es tu edad?"))
espacio = (" ") 
print("Okey, vamos hacer CONDICIONES")

num_uno = int(input("Que number del 1 al 10 estoy pensando?"))

if num_uno == 7 :
    print("Eres muy bueno en esto..")

else:
    print("sigue intentando, no te rindas..")

#sistema para calcular promedio

print(("Vamos a calcular tu promedio ") + nombre)

prom_mate = float(input(nombre + (" Cual es tu promedio en mate?.. no mientas yo lo se todo")))
prom_bio = float(input(nombre + (" Cual es tu promedio en biologia?.. no mientas yo lo se todo")))
prom_fisica = float(input(nombre + (" Cual es tu promedio en fisica?.. no mientas yo lo se todo")))

promedio = float((prom_mate + prom_bio + prom_fisica) / 3)

print(("Tu promedio es de "), int(promedio))
print(("Tu promedio es de "), round(promedio,3))
                    
if promedio >= 7:
    print(("Pasaste el año ") + nombre + (" disfruta tus vacaciones"))
else:
    print(("Te quedaste de año tienes ") + edad + espacio + nombre + ("sigues joven, ahi esta por pasar de vago"))

print("Gracias por utilizar este programa")"""
ingresos = float(input("ingresos del mes"))
num_one = float(input("ingresa el valor"))
operacion = (ingresos -(220.00+180.00)- num_one)
print(("resultados, "),operacion)



