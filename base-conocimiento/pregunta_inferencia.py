# Preguntas -> hechos
preguntas = {
    "cable_desconectado": "¿El cable de alimentación está desconectado?",
    "pitidos_3": "¿El PC emite 3 pitidos al encender?",
    "pantalla_negra": "¿La pantalla permanece negra al encender?"
}

# Reglas simples
reglas = [
    {"if": ["cable_desconectado"], "then": ["sin_energia"]},
    {"if": ["pitidos_3"], "then": ["fallo_memoria"]},
    {"if": ["pantalla_negra"], "then": ["posible_gpu"]},
]

# Motor de inferencia (encadenamiento hacia adelante)
def inferencia(hechos, reglas):
    nuevos = True
    while nuevos:
        nuevos = False
        for regla in reglas:
            if all(cond in hechos for cond in regla["if"]):
                for concl in regla["then"]:
                    if concl not in hechos:
                        hechos.append(concl)
                        nuevos = True
    return hechos

# Programa principal
def ejecutar():
    hechos = []
    print("\n=== Sistema Experto en diagnostico de daños de pc")
    for hecho, pregunta in preguntas.items():
        resp = input(pregunta + " (si/no): ").strip().lower()
        if resp == "si":
            hechos.append(hecho)

    hechos_finales = inferencia(hechos, reglas)

    print("\n--- Diagnóstico ---")
    for f in hechos_finales:
        if f not in preguntas:  # solo mostrar conclusiones
            print(" -", f)

# Ejecutar
ejecutar()