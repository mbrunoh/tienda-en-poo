from os import system
from time import sleep
import pandas as pd
import csv
from herramientas import header

class Producto:
    __productos = {}
    __id = 0
    def __init__(self, nombre, precio, stock):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock
        Producto.__productos[self.__id] = self
        Producto.__id = self.__id + 1
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    @property
    def precio(self):
        return self.__precio
    @precio.setter
    def precio(self, precio):
        self.__precio = precio
    @property
    def stock(self):
        return self.__stock
    @stock.setter
    def stock(self, stock):
        self.__stock = stock
    def __str__(self):
        return f'{self.nombre} | Precio: $ {self.__precio:.2f} | Stock: {self.stock}'
    
    @classmethod
    def lista_productos(self):
        return self.__productos

def buscar_producto(n_producto):
    lista_productos = list(Producto.lista_productos().values())
    for producto in lista_productos:
        if producto.nombre == n_producto:
            return producto
    else:
        return False

def registrar_producto():
    system('clear')
    header('NUEVO PRODUCTO')
    while True:
        nombre = input('Nombre del producto: ').strip().capitalize()
        if not buscar_producto(nombre):
            break
        else:
            print(f'ERROR ---> El producto [{nombre}] ya existe!')
    while True:
        try:
            precio = float(input('Precio: $ '))
        except:
            print('ERROR ---> Precio inválido!')
        else:
            break
    while True:
        try:
            stock = int(input('Cantidad en stock: '))
        except:
            print('ERROR ---> Cantidad inválida!')
        else:
            break
    Producto(nombre, precio, stock)
    system('clear')
    print(f'Producto [{nombre}] registrado con suceso!')
    input('[ENTER]')

def mostrar_productos():
    system('clear')
    header('STOCK')
    lista_productos = list(Producto.lista_productos().values())
    if len(lista_productos) < 1:
        print('No hay productos en la tienda.')
    else:
        for producto in lista_productos:
            print(f'{producto.nombre:8} | Precio: $ {producto.precio:8.2f} | Stock: {producto.stock:3}')
    print()
    input('[ENTER]')

def comprar():
    system('clear')
    header('STOCK DE LA TIENDA')
    while True:
        name = input('¿Que producto desea comprar? ').strip().capitalize()
        producto = buscar_producto(name)
        if not producto:
            print(f'ERROR ---> El producto {name} no existe en la tienda!')
        else:
            break
    while True:
        try:
            cantidad = int(input('Cantidad: '))
        except:
            print('ERROR ---> Cantidad inválida!')
        else:
            break
    producto.stock += cantidad
    print('Compra realizada con suceso!')   
    input('[ENTER]')

def vender():
    system('clear')
    header('VENTA AL CLIENTE')
    while True:
        name = input('¿Que producto desea vender? ').strip().capitalize()
        producto = buscar_producto(name)
        if not producto:
            print(f'ERROR ---> El producto {name} no existe en la tienda!')
        else:
            break
    while True:
        try:
            cantidad = int(input('Cantidad: '))
        except:
            print('ERROR ---> Cantidad inválida!')
        else:
            if producto.stock < cantidad:
                print('No es posible realizar la venta porque no hay cantidad suficiente!')
                print(f'Stock: {producto.stock}')
            else:
                break
    print(f'Usted está vendiendo {cantidad} de {producto.nombre}. El total es: $ {cantidad * producto.precio:.2f}')
    while True:
        opt = input('Confirma la venta? [s/n] ').lower()
        if opt == 's':
            producto.stock -= cantidad
            print('Venta realizada con suceso!')
            break
        elif opt =='n':
            print('La compra no fue realizada!')
            break
    input('[ENTER]')

def archivo_csv(method):
    if method == 'save':
        lista_productos = list(Producto.lista_productos().values())
        df_productos = []
        for producto in lista_productos:
            temp = {
                'nombre':producto.nombre,
                'precio':producto.precio,
                'stock':producto.stock
            }
            df_productos.append(temp)
        df = pd.DataFrame(df_productos)
        df.to_csv('database.csv', index=False)
    elif method == 'load':
        try:
            df = pd.read_csv('database.csv')
        except:
            pass
        else:
            for row in df.itertuples(index=False):
                Producto(row.nombre, row.precio, row.stock)

def edit():
    system('clear')
    header('EDITAR PRODUCTO')
    while True:
        name = input('¿Que producto desea editar? ').strip().capitalize()
        producto = buscar_producto(name)
        if not producto:
            print(f'ERROR ---> El producto {name} no existe en la tienda!')
        else:
            break
    system('clear')
    header(f'{producto.nombre} | Precio: {producto.precio:.2f}')
    print('1 - Nombre')
    print('2 - Precio')
    print()
    while True:
        opc = input('¿Que desea editar?')
        if opc == '1':
            while True:
                nombre = input('Nuevo nombre: ').strip().capitalize()
                if not buscar_producto(nombre):
                    producto.nombre = nombre
                    print('Nombre del producto actualizado con suceso!')
                    break
                else:
                    print('Ya existe un producto con este nombre!')
            break
        elif opc == '2':
            while True:
                try:
                    precio = float(input('Nuevo precio: $ '))
                except:
                    print('Precio inválido!')
                else:
                    producto.precio = precio
                    print('Precio del producto actualizado con suceso!')
                    break
            break
    input('[ENTER]')

def menu():
    while True:
        system('clear')
        header('TIENDA')
        print('1 - Registrar producto')
        print('2 - Vender')
        print('3 - Comprar para Stock')
        print('4 - Stock de productos')
        print('5 - Editar Nombre/Precio')
        print('0 - Salir')
        print()
        opt = input('Opción: ')
        match opt:
            case '1':
                registrar_producto()
            case '2':
                vender()
            case '3':
                comprar()
            case '4':
                mostrar_productos()
            case '5':
                edit()
            case '0':
                archivo_csv('save')
                break
            case _:
                print('ERROR ---> Opción inválida!')
                sleep(0.2)
                pass

archivo_csv('load')

menu()