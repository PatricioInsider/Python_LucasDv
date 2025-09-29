reglas = [
            {
                "condiciones" : ["fiebre" , "tos"],
                "diagnostico": "Podria tener gripe"

            },
            {
                "condiciones": ["dolor de cabeza","fiebre"],
                "diagnostico": "Podría tener dengue"
            },
            {
                "condiciones": ["dolor muscular", "fatiga"],
                "diagnostico": "Podría tener Covid 19"
            }
]

#Bases de hechos (Lo que proporciona el usuario)
hechos = []

#Motor Inferencia
def motor_inferencia(hechos,reglas):
    conclusiones = []
    for regla in reglas:
        if all(condicion in hechos for condicion in regla["condiciones"]):
            conclusiones.append(regla["diagnostico"])
    return conclusiones

#Recolectar datos del usuario
print ("Ingrese uno por uno los sintomas. Escriba fin para terminar")
while True:
    sintoma = input("Sintoma: ").strip().lower()
    if sintoma == "fin":
        break
    hechos.append(sintoma)

#Inferir o deducir el diagnostico
resultado = motor_inferencia(hechos, reglas)

#Mostrar los resultados
print("Su diagnostico es")
if resultado:
    for r in resultado:
        print(f" - {r}")
else:
    print("No se encontró un diagnóstico asociado a los sintomas proporcionados")