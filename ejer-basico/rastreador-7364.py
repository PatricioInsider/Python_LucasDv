
# Autor>Patricio Quishpe 7364
import string

def convertir_minusculas(palabra):
    return palabra.lower()

def comparar_cadenas(a, b):
    return a.lower() == b.lower()

def contar_palabras(texto, palabras_a_rastrear):
    contador = {palabra: 0 for palabra in palabras_a_rastrear}

    texto_limpio = texto.translate(str.maketrans("", "", string.punctuation)).lower()
    palabras = texto_limpio.split()

    for palabra in palabras:
        for palabra_rastrear in palabras_a_rastrear:
            if comparar_cadenas(palabra, palabra_rastrear):
                contador[palabra_rastrear] += 1

    return contador

def main():
    # Texto de entrada
    texto = """
    Del camino a mitad de nuestra vida encontréme por una selva oscura, 
    que de derecha senda era perdida. ¡Y cuánto en el decir es cosa dura 
    esta selva salvaje, áspera y fuerte, que en el pensar renueva la pavura!
    Tanto es amarga que es poco más muerte: más, para hablar del bien que allí encontrara
    diré otras cosas de que fui vidente.
    Yo no se bien decir cómo allí entrara; tan lleno era de sueño en aquel punto que el
    derecho camino abandonara.
    Mas luego, al ser al pie de un monte junto en donde daba término aquel valle que aflicto
    en miedo el corazón me tuvo, miré a lo alto, y vi que era en su talle vestido ya de rayos
    del planeta que nos guía derecho en cualquier calle.
    Fue entonces la pavura un poco quieta, que en el lago del pecho aún me duraba la noche,
    que pasara tanto inquieta.
    Y como aquel que con cansadas ansias, salido ya del piélago a la riba, se vuelve a ver las
    peligrosas aguas, así el ánima mía, aún fugitiva, se volvió atrás a remirar el paso que no
    dejó jamás persona viva.
    """

    palabras_a_rastrear = ["alto", "viva", "persona", "cielo", "ansias"]

    resultado = contar_palabras(texto, palabras_a_rastrear)

    
    print("Ocurrencias de las palabras rastreadas:")
    for palabra, ocurrencias in resultado.items():
        print(f"{palabra}: {ocurrencias}")

if __name__ == "__main__":
    main()
