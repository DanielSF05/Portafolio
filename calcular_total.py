def calcular_total(productos):
    total_general = 0
    for nombre, precio in productos.items():
        cantidad = int(input(f"Ingrese la cantidad para '{nombre}': "))
        total_producto = precio * cantidad
        print(f"Total para {nombre}: {total_producto:.2f}")
        total_general += total_producto
    print(f"\nTotal general: {total_general:.2f}")