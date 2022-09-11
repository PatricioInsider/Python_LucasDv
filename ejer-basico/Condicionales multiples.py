#condiciones logicas multiples
print("TEST PARA VER SI EL O ELLA TE AMA")

principal = input("(No puedes mentir) \nA quien amas?..")
nombre = input(("Quien es el amor de la vida de ") + principal)
contraseña = input(str("contraseña\n"))
nombre = nombre.lower()

if nombre == ("gina canchi") and contraseña == ("14 meses"):
    print(nombre +(" Sabias que el ")+ principal + (" te ama"))
    texto = input("\nQuisieras decirle algo?\n")
elif nombre == ("ingrid veci") and contraseña == ("papipollo"):
    print(nombre + (", cuando vamos a las papas veci, ya te quiero culear"))
elif nombre == ("ambar cando") and contraseña == ("amiga"):
    print(nombre + (" vete demonio"))
else:
    print(("A ti nadie te quire, ") + principal + ("no te ama"))

print("Fin")
print(principal)

#OPCIONES MULTIPLES

            
