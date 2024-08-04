import os
import platform

from Afrodita_GP import (
    Calzado,
    Bikini,
    Gestion_productos,
)1

def limpiar_pantalla():
    ''' Limpiar la pantalla según el sistema operativo'''
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear') # Para Linux/Unix/MacOs

def mostrar_menu():
    print("========== Menú de Gestión de Productos AFRODITA <3 ==========")
    print('1. Agregar Calzado')
    print('2. Agregar Bikini')
    print('3. Buscar producto por código')
    print('4. Actualizar producto')
    print('5. Eliminarar producto por codigo')
    print('6. Mostrar todos los productos')
    print('7. Salir')
    print('==========================<3===========================')

def agregar_producto(gestion, tipo_producto):
    try:
        codigo = int(input('Ingrese codigo del producto: '))
        nombre = input('Ingrese nombre del producto: ')
        precio = float(input('Ingrese precio del producto: '))
        cantidad_stock=int(input('Ingrese cantidad de stock del producto: '))
        talle = int(input('Ingrese talle del producto: '))
        color = str(input('Ingrese color del producto: '))

        if tipo_producto == '1':
            tipo_calzado = input('Ingrese tipo de calzado (sandalia/bota/zapatilla): ')
            producto = Calzado(nombre, codigo, precio, cantidad_stock, talle, color, tipo_calzado)
        elif tipo_producto == '2':
            tipo_bikini = input('Ingrese tipo de cbikini (entera/2 partes/ 3 partes): ')
            producto = Bikini(nombre, codigo, precio, cantidad_stock, talle, color, tipo_bikini)
        else:
            print('Opción inválida')
            return

        gestion.crear_producto(producto)
        input('Presione enter para continuar...')

    except ValueError as e:
        print(f'Error: {e}')
    except Exception as e:
        print(f'Error inesperado: {e}')

def buscar_producto_por_COD(gestion):
    codigo = input('Ingrese el COD del producto a buscar: ')
    gestion.leer_producto(codigo)
    input('Presione enter para continuar...')

def actualizar_precio_producto(gestion):
    codigo = input('Ingrese el COD del producto para actualizar el precio de venta: ')
    precio = float(input('Ingrese el precio del producto'))
    gestion.actualizar_producto(codigo, precio)
    input('Presione enter para continuar...')

def eliminar_producto_por_COD(gestion):
    codigo = input('Ingrese el COD del producto a eliminar: ')
    gestion.eliminar_producto(codigo)
    input('Presione enter para continuar...')

def mostrar_todos_los_productos(gestion):
    print('=============== Listado completo de los  Productos ==============')
    for producto in gestion.leer_datos().values():
        if 'tipo_calzado' in producto:
            print(f"{producto['nombre']} - Tipo {producto['tipo_calzado']}")
        else:
            print(f"{producto['nombre']} - Tipo {producto['tipo_bikini']}")
    print('================================<3====================================')
    input('Presione enter para continuar...')

if __name__ == "__main__":
    archivo_productos = 'productos_db.json'
    gestion = Gestion_productos(archivo_productos)

    while True:
        limpiar_pantalla()
        mostrar_menu()
        opcion = input('Seleccione una opción: ')

        if opcion == '1' or opcion == '2':
            agregar_producto(gestion, opcion)
        
        elif opcion == '3':
            buscar_producto_por_COD(gestion)

        elif opcion == '4':
            actualizar_precio_producto(gestion)

        elif opcion == '5':
            eliminar_producto_por_COD(gestion)

        elif opcion == '6':
            mostrar_todos_los_productos(gestion)

        elif opcion == '7':
            print('Saliendo del programa...')
            break
        else:
            print('Opción no válida. Por favor, seleccione una opción válida (1-7)')
        
