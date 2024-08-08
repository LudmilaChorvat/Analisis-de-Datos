'''
Desafío 1: Sistema de Gestión de Productos
Objetivo: Desarrollar un sistema para manejar productos en un inventario.

Requisitos:

Crear una clase base Producto con atributos como nombre, precio, cantidad en stock, etc.
Definir al menos 2 clases derivadas para diferentes categorías de productos (por ejemplo, ProductoElectronico, ProductoAlimenticio) con atributos y métodos específicos.
Implementar operaciones CRUD para gestionar productos del inventario.
Manejar errores con bloques try-except para validar entradas y gestionar excepciones.
Persistir los datos en archivo JSON.
'''
import json

class Producto:
    def __init__(self, nombre, codigo,  precio, cantidad_stock, talle):     #Construyo la clase
        self.__nombre = nombre                                              #Defino los atributos
        self.__codigo=self.validar_codigo(codigo)                           #Con doble guion bajo los atributos son privados para protegerlos
        self.__precio = self.validar_precio(precio)
        self.__cantidad_stock = self.validar_cantidad_stock(cantidad_stock)
        self.__talle= talle

    @property                                                               #Con property defino las propiedades para que puedan ser utilizadas por subclases. Las vuelvo accesibles y tratables. 
    def nombre(self):                                                       # Puedo aplicar tratamientos a la ingo que to deseo devolver.
        return self.__nombre                                                # Por ejemplo, podría devolver el precio de venta y no el precio de costo 
    
    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def precio(self):
        return self.__precio
    
    @property
    def cantidad_stock(self):
        return self.__cantidad_stock
    
    @property
    def talle(self):
        return self.__talle
    
    @codigo.setter
    def codigo(self, nuevo_codigo):
        self.__codigo=self.validar_codigo(nuevo_codigo)
    
    def validar_codigo(self, codigo):
        try:
            codigo= int(codigo)
            if len(str(codigo)) != 4:
                raise ValueError("El codigo debe tener 4 digitos")
            if codigo < 0:
                raise ValueError("El codigo no puede ser un número negativo")
            return codigo
        except ValueError:
            raise ValueError("El codigo debe ser un numero válido")


    @precio.setter                                                            #Sirve para modificar datos resguardados, por ejemplo el COD 
    def precio(self, nuevo_precio):
        self.__precio = self.validar_precio(nuevo_precio)                     #Creo un nuevo metodo que afecte a el atributo. Ej: Validad_precio
    
    def validar_precio(self, precio):
        try:
            precio_art= float(precio)
            if precio_art <= 0:
                raise ValueError("El precio debe ser un valor positivo")
            return round(precio_art,2)
        except ValueError:
            raise ValueError("El precio debe ser un valor numérico.")
    
    @cantidad_stock.setter
    def cantidad_stock(self, nuevo_stock):
        self.__cantidad_stock=self.validar_cantidad_stock(nuevo_stock)

    def validar_cantidad_stock(self, cantidad_stock):
        try:
            cantidad_stock= int(cantidad_stock)
            if cantidad_stock < 0:
                raise ValueError("La cantidad en stock no puede ser un número negativo")
            return cantidad_stock
        except ValueError:
            raise ValueError("La cantidad en stock debe ser un número válido.")

    def to_dict(self):                                      #Retorna todos los atributos como un diccionario
        return {
            "nombre": self.nombre,
            "codigo":self.codigo,
            "precio": self.precio,
            "cantidad_stock": self.cantidad_stock,
            "talle": self.talle
        }

    def __str__(self):                                      #Cuando imprime da una cadema de texto con el nombre del articulo y su codigo
        return f"{self.nombre} - COD:{self.codigo}"

class Calzado(Producto):      
    def __init__(self, nombre, codigo, precio, cantidad_stock, talle, color, tipo_calzado):
        super().__init__(nombre, codigo, precio, cantidad_stock, talle)                 #Super (clase superior) se usa para heredar atributos de la clase Productos 
        self.__tipo_calzado = tipo_calzado
        self.__color= color

    @property
    def tipo_calzado(self):
        return self.__tipo_calzado
    
    @property
    def color(self):
        return self.__color

    def to_dict(self):
        data = super().to_dict()                    #Guarda en una variable llamada data la info to dict de la super clase. Llevan parentesisi porque son metods
        data["tipo"] = self.tipo_calzado            #Agrego las variables que tambien queiro que guarde en el dict
        data["color"]= self.color
        return data

    def __str__(self):
        return f"{super().__str__()} - Tipo de calzado: {self.tipo_calzado} y color: {self.color}"

class Bikini(Producto):
    def __init__(self,nombre, codigo, precio, cantidad_stock, talle, color, tipo_bikini ):
        super().__init__(nombre, codigo, precio, cantidad_stock, talle)
        self.__tipo_bikini = tipo_bikini
        self.__color=color

    @property
    def tipo_bikini(self):
        return self.__tipo_bikini
    
    @property
    def color(self):
        return self.__color

    def to_dict(self):
        data = super().to_dict()
        data["tipo_bikini"] = self.tipo_bikini
        data["color"]=self.color
        return data

    def __str__(self):
        return f"{super().__str__()} - Tipo de Bikini: {self.tipo_bikini} - Color: {self.color}"

class Gestion_productos:                                                    #En esta clase se crea el CRUD
    def __init__(self, archivo):
        self.archivo = archivo

    def leer_datos(self):
        try:
            with open(self.archivo, 'r') as file:                          #abrimos el archivo en forma de lectura como file
                datos = json.load(file)                                    #el load toma el archivo json y disponibiliza para leerlo y modificarlo en py
        except FileNotFoundError:                                          #Si no se encuentra el archivo retorna un diccionario vacío
            return {}
        except Exception as error:
            raise Exception(f'Error al leer datos del archivo: {error}')   #Me dice el error ocurrido
        else:
            return datos

    def guardar_datos(self, datos):
        try:
            with open(self.archivo, 'w') as file:
                json.dump(datos, file, indent=4)                       # dump lo que hace es transofrmar el archivo py a json para poder guardarlo. Con ident digo cuantos espacios separa cada cosa 
        except IOError as error:
            print(f'Error al intentar guardar los datos en {self.archivo}: {error}')
        except Exception as error:
            print(f'Error inesperado: {error}')

    def crear_producto(self, producto):
        try:
            datos = self.leer_datos()
            codigo = producto.codigo
            if not str(codigo) in datos.keys():                #Uso keys para acceder a los valores guardados en "codigo" para cada producto en funcion del codigo de cada uno
                datos[codigo] = producto.to_dict()             #Usa el metodo creado al inicio para no volver a escribirlo
                self.guardar_datos(datos)
                print(f"Producto {producto.nombre} - COD: {producto.codigo} creado correctamente.")
            else:
                print(f"Ya existe producto con código '{codigo}'.")
        except Exception as error:
            print(f'Error inesperado al crear el producto deseado: {error}')

    def leer_producto(self, codigo):
        try:
            datos = self.leer_datos()
            if codigo in datos:
                producto_data = datos[codigo]
                if 'tipo_calzado' in producto_data:
                    producto = Calzado(**producto_data)
                else:
                    producto = Bikini(**producto_data)
                print(f'Producto {producto} encontrado con código: {codigo}')
            else:
                print(f'No se encontró producto con código: {codigo}')

        except Exception as e: 
            print('Error al leer producto: {e}')

    def actualizar_producto(self, codigo, nuevo_precio):
        try:
            datos = self.leer_datos()
            if str(codigo) in datos.keys():
                 datos[codigo]['precio'] = nuevo_precio
                 self.guardar_datos(datos)
                 print(f'Precio actializado para el producto con código:{codigo}')
            else:
                print(f'No se encontró producto con código:{codigo}')
        except Exception as e:
            print(f'Error al actualizar producto: {e}')

    def eliminar_producto(self, codigo):
        try:
            datos = self.leer_datos()
            if str(codigo) in datos.keys():
                 del datos[codigo]
                 self.guardar_datos(datos)
                 print(f'Producto con COD:{codigo} eliminado correctamente')
            else:
                print(f'No se encontró producto con COD:{codigo}')
        except Exception as e:
            print(f'Error al eliminar el producto: {e}')
    def mostrar_productos(self):
        try:
            datos = self.leer_datos()
            if datos:
                print('=============== Listado de Stock Disponible ==============')
                for codigo, producto_data in datos.items():
                    print(f"COD: {codigo}")
                    print(f"  Nombre: {producto_data['nombre']}")
                    print(f"  Precio: {producto_data['precio']}")
                    print(f"  Cantidad Total: {producto_data['cantidad_stock']}")
                    print(f" Talle: {producto_data['talle']}")
                    print(f" Tipo: {producto_data['tipo']}")
                    print(f" Color: {producto_data['color']}")
                    
                print('=========================<3===============================')
            else:
                print('No hay Stock disponible .')
        except Exception as e:
            print(f'Error : {e}')