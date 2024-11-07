# Inicializar las ventas totales
ventasTotales = 0.0

# Solicitar el número de productos
numProductos = int(input('Ingrese el número de productos a gestionar: '))

# Listas para almacenar la información
nombres = []
precios = []
cantidades = []

print('Ingreso de productos iniciales a la tienda:')
for i in range(numProductos):
    print(f'Producto {i+1}:')
    nombre = input('Ingrese el nombre del producto: ').lower()
    nombres.append(nombre)
    precio = float(input('Ingrese el precio del producto: '))
    precios.append(precio)  
    cantidad = int(input('Ingrese la cantidad del producto: '))  # Convertir a int
    cantidades.append(cantidad)

# Ciclo principal del menú
while True:
    print('\n--- MENÚ DE GESTIÓN DROGUERÍA ---')
    print('1. Vender producto')
    print('2. Mostrar producto')
    print('3. Mostrar ventas totales')
    print('4. Salir')

    opcion = int(input('Ingrese una opción: '))

    if opcion == 1:
        print('\nVender producto')
        nombreVenta = input('Ingrese el nombre del producto a vender: ').lower()
        cantidadVender = int(input('Ingrese la cantidad a vender: '))
        productoEncontrado = False

        for i in range(len(nombres)):
            if nombres[i] == nombreVenta:
                productoEncontrado = True
                if cantidadVender <= cantidades[i]:
                    totalVenta = cantidadVender * precios[i]
                    ventasTotales += totalVenta
                    cantidades[i] -= cantidadVender
                    print(f'Venta realizada. Total de esta venta: ${totalVenta:.2f}')
                    print(f'Quedan {cantidades[i]} unidades de {nombres[i]} en el inventario')
                else:
                    print(f'Cantidad insuficiente en el inventario; solo hay {cantidades[i]} unidades disponibles.')
                break  # Salir del bucle una vez encontrado el producto

        if not productoEncontrado:
            print('Producto no encontrado en el inventario')

    elif opcion == 2:
        print('\nInventario de productos')
        for i in range(len(nombres)):
            print(f'Producto {i+1}: {nombres[i].capitalize()}, Precio: ${precios[i]:.2f}, Cantidad: {cantidades[i]}')

    elif opcion == 3:
        print(f'\nVentas totales acumuladas: ${ventasTotales:.2f}')

    elif opcion == 4:
        print('Gracias por usar el sistema de gestión de droguerías.')
        break

    else: 
        print('Opción inválida, por favor ingrese un número entre 1 y 4')
