#Patricio Quishpe base de conocimiento
#herramienta de apoyo para deteccion de correos falsos
# --- BASE DE HECHOS ---
hechos = {
    "tiene_enlace_sospechoso": None,    
    "dominio_desconocido": None,        
    "solicita_datos_personales": None,  
    "urgencia_mensaje": None,           
    "errores_ortograficos": None,       
    "archivo_adjunto": None,            
    "promesa_dinero": None,             
    "imitacion_empresa": None,          
    "direccion_remitente_rara": None,   
    "mensaje_no_esperado": None         
}

reglas = [
    {
        "si": [("tiene_enlace_sospechoso", "si"), ("dominio_desconocido", "si")],
        "entonces": ("diagnostico", "El correo podría ser phishing: el enlace lleva a un dominio desconocido.")
    },
    {
        "si": [("solicita_datos_personales", "si"), ("urgencia_mensaje", "si")],
        "entonces": ("diagnostico", "Alerta de phishing: intenta robar credenciales usando urgencia.")
    },
    {
        "si": [("errores_ortograficos", "si"), ("imitacion_empresa", "si")],
        "entonces": ("diagnostico", "Probable phishing: imita a una empresa pero con errores de redacción.")
    },
    {
        "si": [("archivo_adjunto", "si"), ("mensaje_no_esperado", "si")],
        "entonces": ("diagnostico", "Riesgo de malware: archivo adjunto sospechoso en correo no esperado.")
    },
    {
        "si": [("promesa_dinero", "si")],
        "entonces": ("diagnostico", "Phishing clásico: promesa de dinero fácil.")
    },
    {
        "si": [("imitacion_empresa", "si"), ("direccion_remitente_rara", "si")],
        "entonces": ("diagnostico", "Phishing: suplantación de identidad de empresa con remitente falso.")
    },
    {
        "si": [("tiene_enlace_sospechoso", "si"), ("urgencia_mensaje", "si")],
        "entonces": ("diagnostico", "Phishing: enlace fraudulento con presión psicológica de urgencia.")
    },
    {
        "si": [("mensaje_no_esperado", "si"), ("direccion_remitente_rara", "si")],
        "entonces": ("diagnostico", "Phishing potencial: correo no esperado de dirección extraña.")
    },
    {
        "si": [("archivo_adjunto", "si"), ("errores_ortograficos", "si")],
        "entonces": ("diagnostico", "Phishing con malware: archivo adjunto disfrazado con mensaje mal escrito.")
    },
    {
        "si": [("tiene_enlace_sospechoso", "si"), ("promesa_dinero", "si")],
        "entonces": ("diagnostico", "Phishing: enlace sospechoso que promete dinero o premios falsos.")
    },
    {
        "si": [("solicita_datos_personales", "si"), ("mensaje_no_esperado", "si")],
        "entonces": ("diagnostico", "Phishing: solicita datos personales en correo inesperado.")
    },
    {
        "si": [("promesa_dinero", "si"), ("direccion_remitente_rara", "si")],
        "entonces": ("diagnostico", "Estafa por promesa de dinero: remitente poco creíble.")
    },
    {
        "si": [("archivo_adjunto", "si"), ("dominio_desconocido", "si")],
        "entonces": ("diagnostico", "Posible malware: adjunto proveniente de un dominio desconocido.")
    },
    {
        "si": [("urgencia_mensaje", "si"), ("errores_ortograficos", "si")],
        "entonces": ("diagnostico", "Phishing urgente con redacción pobre: posible intento de engaño.")
    }
]

# --- MOTOR DE INFERENCIA (muestra todos los diagnósticos) ---
def motor_de_inferencia_multiple(hechos, reglas):
    diagnósticos = []        
    reglas_activadas = []  

    for regla in reglas:
        # Verificamos si todas las condiciones de la regla se cumplen con los hechos actuales
        if all(hechos.get(k) == v for k, v in regla["si"]):
            # Si la regla se cumple, obtenemos la conclusión (diagnóstico)
            conclusion_clave, conclusion_valor = regla["entonces"]

            # Agregamos el diagnóstico solo si aún no está en la lista
            if conclusion_valor not in diagnósticos:
                diagnósticos.append(conclusion_valor)   
                reglas_activadas.append(regla)       
    return diagnósticos, reglas_activadas


def iniciar_diagnostico():
    print("--- Sistema Experto para Detección de Phishing ---")
    print("Responde 'si' o 'no' a las siguientes preguntas:")

    hechos["tiene_enlace_sospechoso"] = input("¿El correo contiene un enlace sospechoso? (ej. link extraño) ").strip().lower()
    hechos["dominio_desconocido"] = input("¿El dominio del enlace o remitente es desconocido? (ej. no es gmail.com) ").strip().lower()
    hechos["solicita_datos_personales"] = input("¿El correo pide datos personales o contraseñas? (ej. tu clave bancaria) ").strip().lower()
    hechos["urgencia_mensaje"] = input("¿El mensaje transmite urgencia? (ej. 'última oportunidad') ").strip().lower()
    hechos["errores_ortograficos"] = input("¿El correo tiene errores de ortografía? (ej. 'Bonoo disponible') ").strip().lower()
    hechos["archivo_adjunto"] = input("¿El correo trae un archivo adjunto? (ej. .exe, .docm) ").strip().lower()
    hechos["promesa_dinero"] = input("¿El correo promete dinero o premios? (ej. 'Ganaste $1000') ").strip().lower()
    hechos["imitacion_empresa"] = input("¿El correo dice ser de una empresa conocida? (ej. Banco XYZ) ").strip().lower()
    hechos["direccion_remitente_rara"] = input("¿El remitente tiene una dirección rara o poco creíble? (ej. xyz@abc123.com) ").strip().lower()
    hechos["mensaje_no_esperado"] = input("¿El correo es inesperado? (ej. no estabas esperando este email) ").strip().lower()

    print("\nHechos recolectados:", {k:v for k,v in hechos.items() if v is not None})
    print("\nRazonando...\n")

    diagnósticos, reglas_activadas = motor_de_inferencia_multiple(hechos, reglas)

    for r in reglas_activadas:
        print(f"Regla aplicada: SI {r['si']} ENTONCES {r['entonces']}")

    print("\nDiagnósticos encontrados:")
    if diagnósticos:
        for d in diagnósticos:
            print(" -", d)
    else:
        print(" No se detectó un patrón claro de phishing con la información dada.")

iniciar_diagnostico()
