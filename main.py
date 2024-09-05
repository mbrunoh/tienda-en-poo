from os import system
from time import sleep
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
    @property
    def precio(self):
        return self.__precio
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

Producto('Banana', 50.00, 5)
Producto('Manzana', 100.00, 15)
Producto('Uva', 1850.00, 10)

def buscar_producto(n_producto):
    lista_productos = list(Producto.lista_productos().values())
    for producto in lista_productos:
        if producto.nombre == n_producto:
            return producto
    else:
        return False

def registrar_producto():
    system('clear')
    header('REGISTRAR NUEVO PRODUCTO')
    while True:
        nombre = input('Nombre del producto: ').strip().capitalize()
        if not buscar_producto(nombre):
            break
        else:
            print(f'ERROR ---> El producto [{nombre}] ya existe!')
    while True:
        try:
            precio = float(input('Precio: '))
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
            cantidad = int(input('¿Que cantidad desea comprar? '))
        except:
            print('ERROR ---> Cantidad inválida!')
        else:
            break
    print(f'Usted está comprando {cantidad} de {producto.nombre}. El total es: $ {cantidad * producto.precio:.2f}')
    while True:
        opt = input('Confirma la compra? [s/n] ').lower()
        if opt == 's':
            producto.stock = producto.stock + cantidad
            print('Compra realizada con suceso!')
            break
        elif opt =='n':
            print('La compra no fue realizada!')
            break
    
    input('[ENTER]')

def menu():
    while True:
        system('clear')
        header('TIENDA')
        print('1 - Registrar producto')
        print('2 - Vender')
        print('3 - Comprar')
        print('4 - Stock de productos')
        print('0 - Salir')
        print()
        opt = input('Opción: ')
        match opt:
            case '1':
                registrar_producto()
            case '2':
                pass
            case '3':
                comprar()
            case '4':
                mostrar_productos()
            case '0':
                break
            case _:
                print('ERROR ---> Opción inválida!')
                sleep(0.2)
                pass

menu()