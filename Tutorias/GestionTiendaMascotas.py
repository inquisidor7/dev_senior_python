from datetime import datetime

#variables temporales
inventario = []
ventas = []
ventas_totales_acumuladas = 0

while True:
    print("--- MENU GESTION MASCOTAS ---")
    print("1. agregar un producto al inventario")
    print("2. vender un producto")
    print("3. mostrar el inventario detallado")
    print("4. historia de ventas")
    print("5. mostrar ventas totales")
    print("6. Salir")
    
    opcion = input("seleccione una opcion: ")
    
    if opcion == "1":
        nombre = input("ingrese el nombre del producto")
        categoria = input("ingrese la categoria del producto: ")
        precio = float(input("ingrese el precio del producto: "))
        cantidad = int(input("ingrese la cantidad del producto: "))
        fecha_ingreso = datetime.now().strftime("%Y-%m-%d")
        
        producto = [nombre, categoria, precio, cantidad, fecha_ingreso]
        inventario.append(producto)
        print("el producto ha sido agregado al inventario")
        
    elif opcion == "2":
        print("VENTAS DE PRODUCTO")
        nombre = input("ingrese el nombre del producto:").lower()
        cantidad_vender = int(input("ingrese la cantidad a vender: "))
        producto_encontrado = False
        for producto in inventario:
            if producto[0] == nombre:
                producto_encontrado = True
                if producto[3] >= cantidad_vender:
                    total = producto[2] * cantidad_vender
                    producto[3] -= cantidad_vender
                    ventas.append([nombre, cantidad_vender, total])
                    ventas_totales_acumuladas += total
                    print("se ha vendido el producto")
                else:
                    print("no hay suficientes productos en inventario")
                    break
            if not producto_encontrado:
                print("el producto no se encuentra en inventario")
                
    elif opcion == "3":
        if inventario:
            print("-------------------")
            print("inventario")
            print("-------------------")
            for producto in inventario:
                print(f"nombre: {producto[0]}")
                print(f"categoria: {producto[1]}")
                print(f"precio: {producto[2]}")
                print(f"cantidad: {producto[3]}")
                print(f"fecha de ingreso: {producto[4]}")
                
    elif opcion == "4":
        pass
    elif opcion == "5":
        pass
    elif opcion == "6" or opcion == "salir":
        print("gracias por usar gestion de mascotas")
        break
    else:
        print("opcion invalida por favor ingrese una opcion entre 1 y 6")
        