import datetime

# ==========================================
# ESTRUCTURAS DE DATOS (Variables Globales)
# ==========================================
# Listas que contendrán diccionarios
productos = []
proveedores = []
movimientos = []

# ==========================================
# FUNCIONES AUXILIARES
# ==========================================
def buscar_producto(dato_busqueda):
    """Busca un producto por código o nombre y retorna el diccionario si lo encuentra."""
    for prod in productos:
        if str(prod['codigo']) == str(dato_busqueda) or prod['nombre'].lower() == str(dato_busqueda).lower():
            return prod
    return None

# ==========================================
# FUNCIONES DEL MENÚ
# ==========================================
def registrar_producto():
    codigo = input("ingrese el codigo del producto: ")
    nombre = input("Ingrese el nombre del producto: ")
    descripcion = input("Ingrese la descripción: ")
    categoria = input("Ingrese la Categoría: ")
    
    # Validamos que el precio sea solo número
    while True:
        try:
            precio = float(input("Precio (solo números): "))
            break
        except ValueError:
            print("[Error] Ingresa un número válido (ej: 6.00 o 45.50).")
            
    cantidad = int(input("Cantidad inicial: "))
    

    unidad_medida = input("Unidad de medida (ej: libra, galón, unidad): ")
    
    proveedor = input("Proveedor: ")

    nuevo_producto = {
        'codigo': codigo, 
        'nombre': nombre,
        'descripcion': descripcion,
        'categoria': categoria,
        'precio': precio,
        'cantidad': cantidad,
        'unidad_medida': unidad_medida, 
        'proveedor': proveedor
    }

    productos.append(nuevo_producto)
    print("[OK] Producto registrado correctamente.")


def registrar_proveedor():
    print("\n--- REGISTRAR PROVEEDOR ---")
    nombre = input("Nombre del proveedor: ")
    
    # Verificar si existe
    for prov in proveedores:
        if prov['nombre'].lower() == nombre.lower():
            print("Error: Proveedor ya registrado.")
            return

    contacto = input("Contacto del proveedor (Tel/Correo): ")
    proveedores.append({'nombre': nombre, 'contacto': contacto})
    print("[OK] Proveedor registrado correctamente.")

def registrar_entrada():
    print("\n--- REGISTRAR ENTRADA ---")
    dato = input("Código o nombre del producto a buscar: ")
    producto = buscar_producto(dato)
    
    if producto:
        cantidad_entrada = int(input("Cantidad de entrada: "))
        producto['cantidad'] += cantidad_entrada
        
        fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        movimientos.append({
            'fecha': fecha,
            'codigo': producto['codigo'],
            'tipo': 'ENTRADA',
            'cantidad': cantidad_entrada
        })
        print(f"[OK] Entrada registrada. Nueva existencia: {producto['cantidad']}")
    else:
        print("[X] Producto no encontrado.")

def registrar_salida():
    print("\n--- REGISTRAR SALIDA ---")
    dato = input("Código o nombre del producto a buscar: ")
    producto = buscar_producto(dato)
    
    if producto:
        cantidad_salida = int(input("Cantidad de salida: "))
        
        if cantidad_salida <= producto['cantidad']:
            producto['cantidad'] -= cantidad_salida
            fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            movimientos.append({
                'fecha': fecha,
                'codigo': producto['codigo'],
                'tipo': 'SALIDA',
                'cantidad': cantidad_salida
            })
            print(f"[OK] Salida registrada. Nueva existencia: {producto['cantidad']}")
        else:
            print("[X] Error: No hay suficientes existencias.")
    else:
        print("[X] Producto no encontrado.")

def actualizar_existencias():
    print("\n--- ACTUALIZAR EXISTENCIAS MANUALMENTE ---")
    dato = input("Código o nombre del producto a buscar: ")
    producto = buscar_producto(dato)
    
    if producto:
        print(f"Existencia actual: {producto['cantidad']}")
        tipo = input("Tipo de movimiento (ENTRADA/SALIDA): ").upper()
        cantidad = int(input("Cantidad: "))
        
        if tipo == "ENTRADA":
            producto['cantidad'] += cantidad
            print(f"[OK] Existencia actualizada: {producto['cantidad']}")
        elif tipo == "SALIDA":
            if cantidad <= producto['cantidad']:
                producto['cantidad'] -= cantidad
                print(f"[OK] Existencia actualizada: {producto['cantidad']}")
            else:
                print("[X] Error: No hay suficientes existencias para esa salida.")
        else:
            print("[X] Tipo de movimiento no válido.")
    else:
        print("[X] Producto no encontrado.")

def buscar_productos():
    print("\n--- BUSCAR PRODUCTO ---")
    dato = input("Código o nombre del producto a buscar: ")
    producto = buscar_producto(dato)
    
    if producto:
        print("\n--- Datos del Producto ---")
        for clave, valor in producto.items():
            print(f"{clave.capitalize()}: {valor}")
    else:
        print("[X] Producto no encontrado.")

def consultar_existencias():
    print("\n--- CONSULTAR EXISTENCIAS ---")
    dato = input("Código o nombre del producto a buscar: ")
    producto = buscar_producto(dato)
    
    if producto:
        print(f"Producto: {producto['nombre']}")
        print(f"Existencia disponible: {producto['cantidad']}")
    else:
        print("[X] Producto no encontrado.")

def mostrar_productos_agotados():
    print("\n--- PRODUCTOS AGOTADOS ---")
    agotados = [p for p in productos if p['cantidad'] == 0]
    
    if agotados:
        for p in agotados:
            print(f"Código: {p['codigo']} | Nombre: {p['nombre']} | Categoría: {p['categoria']}")
    else:
        print("[OK] No hay productos agotados.")

def mostrar_inventario_general():
    print("\n--- INVENTARIO GENERAL ---")
    if not productos:
        print("El inventario está vacío.")
    else:
        for p in productos:
            print("-" * 30)
            for clave, valor in p.items():
                print(f"{clave.capitalize()}: {valor}")

def generar_reporte_movimientos():
    print("\n--- REPORTE DE MOVIMIENTOS ---")
    if not movimientos:
        print("No hay movimientos registrados.")
    else:
        for mov in movimientos:
            print("-" * 30)
            for clave, valor in mov.items():
                print(f"{clave.capitalize()}: {valor}")

# ==========================================
# MENÚ PRINCIPAL
# ==========================================
def main():
    while True:
        print("\n====================================")
        print("  SISTEMA DE GESTIÓN DE INVENTARIO")
        print("====================================")
        print("1. Registrar productos")
        print("2. Registrar proveedores")
        print("3. Registrar entradas")
        print("4. Registrar salidas")
        print("5. Actualizar existencias")
        print("6. Buscar productos")
        print("7. Consultar existencias")
        print("8. Mostrar productos agotados")
        print("9. Mostrar inventario general")
        print("10. Generar reporte de movimientos")
        print("0. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == '1':
            registrar_producto()
        elif opcion == '2':
            registrar_proveedor()
        elif opcion == '3':
            registrar_entrada()
        elif opcion == '4':
            registrar_salida()
        elif opcion == '5':
            actualizar_existencias()
        elif opcion == '6':
            buscar_productos()
        elif opcion == '7':
            consultar_existencias()
        elif opcion == '8':
            mostrar_productos_agotados()
        elif opcion == '9':
            mostrar_inventario_general()
        elif opcion == '10':
            generar_reporte_movimientos()
        elif opcion == '0':
            print("Programa finalizado. ¡Hasta luego!")
            break
        else:
            print("[X] Opción no válida. Intente de nuevo.")

# Ejecución del programa
if __name__ == "__main__":
    main()
