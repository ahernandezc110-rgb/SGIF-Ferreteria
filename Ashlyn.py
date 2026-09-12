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
               'fecha': fecha, 'codigo': producto['codigo'],
               'tipo': 'SALIDA', 'cantidad': cantidad_salida
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