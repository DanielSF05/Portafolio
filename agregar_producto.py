def agregar_producto(productos):
    nombre = input("Ingrese el nombre del producto: ").strip()
    precio = float(input("Ingrese el precio unitario: "))
    productos[nombre.upper()] = precio