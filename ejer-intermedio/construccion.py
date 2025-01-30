# Punto de inicio y estructura principal del programa
def main():
    # Introducción al programa
    print("=== Sistema de Gestión de Ventas de Automóviles ===\n")
    
    # Base de datos simulada (listas) para automóviles disponibles y vendidos
    autos_disponibles = [
        {"id": 1, "modelo": "Toyota Corolla", "precio": 20000, "stock": 5},
        {"id": 2, "modelo": "Honda Civic", "precio": 22000, "stock": 3},
        {"id": 3, "modelo": "Ford Mustang", "precio": 35000, "stock": 2}
    ]
    autos_vendidos = []

    # Menú principal (con ciclos y funciones)
    while True:
        print("\nOpciones:")
        print("1. Mostrar autos disponibles")
        print("2. Registrar venta de auto")
        print("3. Mostrar autos vendidos")
        print("4. Salir")
        
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            mostrar_autos(autos_disponibles)
        elif opcion == "2":
            registrar_venta(autos_disponibles, autos_vendidos)
        elif opcion == "3":
            mostrar_autos_vendidos(autos_vendidos)
        elif opcion == "4":
            print("Gracias por usar el sistema de gestión de ventas. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

# Función para mostrar autos disponibles
def mostrar_autos(autos_disponibles):
    print("\n=== Autos Disponibles ===")
    if not autos_disponibles:
        print("No hay autos disponibles.")
    else:
        for auto in autos_disponibles:
            print(f"ID: {auto['id']}, Modelo: {auto['modelo']}, Precio: ${auto['precio']}, Stock: {auto['stock']}")

# Función para registrar una venta
def registrar_venta(autos_disponibles, autos_vendidos):
    mostrar_autos(autos_disponibles)
    try:
        id_auto = int(input("\nIngresa el ID del auto que deseas vender: "))
        auto_seleccionado = next((auto for auto in autos_disponibles if auto["id"] == id_auto), None)
        
        if auto_seleccionado and auto_seleccionado["stock"] > 0:
            cantidad = int(input(f"¿Cuántos {auto_seleccionado['modelo']} deseas vender? "))
            if cantidad <= auto_seleccionado["stock"]:
                auto_seleccionado["stock"] -= cantidad
                autos_vendidos.append({"modelo": auto_seleccionado["modelo"], "cantidad": cantidad, "total": cantidad * auto_seleccionado["precio"]})
                print(f"Se ha registrado la venta de {cantidad} {auto_seleccionado['modelo']} por un total de ${cantidad * auto_seleccionado['precio']}.")
            else:
                print("No hay suficiente stock para completar la venta.")
        else:
            print("El ID ingresado no es válido o el auto no está disponible.")
    except ValueError:
        print("Entrada no válida. Por favor, ingresa un número.")

# Función para mostrar autos vendidos
def mostrar_autos_vendidos(autos_vendidos):
    print("\n=== Autos Vendidos ===")
    if not autos_vendidos:
        print("No se han registrado ventas.")
    else:
        for venta in autos_vendidos:
            print(f"Modelo: {venta['modelo']}, Cantidad: {venta['cantidad']}, Total: ${venta['total']}")

# Ejecución principal del programa
if __name__ == "__main__":
    print("hola como estas")
    main()