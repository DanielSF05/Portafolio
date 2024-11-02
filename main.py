from agregar_producto import agregar_producto
from calcular_total import calcular_total
def menu():
    productos = {}
    while True:
        print("\n1. Agregar producto")
        print("2. Calcular total")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_producto(productos)
        elif opcion == '2':
            if productos:
                calcular_total(productos)
            else:
                print("No hay productos agregados.")
        elif opcion == '3':
            print("Saliendo del menú.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu()