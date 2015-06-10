#coding:utf8
"""Register Machine"""
ARTICULOS = {'Manzana':1.25, 'Pera':2.00, 'Sandia':10, 'Naranja':2.00,
            'Mango':3.00,'Banano':1.00, 'Melon':5, 'Piña':5,}
ARTICULOS_EN_INVENTARIO = {}
CANTIDAD_DE_ARTICULOS = {}


#while True:
def ingresando_articulos():
    """Pedira al ususario ingresar un articulo."""
    respuesta_de_usuario = raw_input("Add an item: ")
    respuesta_de_usuario = respuesta_de_usuario.lower()
    return respuesta_de_usuario


def ingresando_precio():
    while True:
        try:
            definiendo_precio = float(raw_input("Ingresar precio: "))
            return definiendo_precio
            break
        except:
            print "No es un numero"

def ingresando_cantidad():
    while True:
        try:
            definiendo_precio = int(raw_input("Ingresar cantidad: "))
            return definiendo_precio
            break
        except:
            print "No es un numero"

def funciones_agregar_item():
    articulo = ingresando_articulos()
    precio = ingresando_precio()
    cantidad = ingresando_cantidad()
    guardar_articulo(articulo, precio, cantidad)


def guardar_articulo(articulo, precio, cantidad):
    ARTICULOS_EN_INVENTARIO[articulo] = precio
    CANTIDAD_DE_ARTICULOS[articulo] = cantidad
    print ARTICULOS_EN_INVENTARIO
    print ""
    print CANTIDAD_DE_ARTICULOS
    print " "
    pregunta_si_o_no()


def pregunta_si_o_no():
    while True:
        print "  Quiere ingresar otro articulo??"
        respuesta_usuario = raw_input("si/no: ")
        if respuesta_usuario == "si":
            print ""
            funciones_agregar_item()
            break
        elif respuesta_usuario == "no":
            print " "
            menu()
            break
        else:
            print "Opcion Invalida , inserte si o no"


def vender_articulos():
    while True:
        print""
        vender_articulos_respuesta = ingresando_articulos()
        if vender_articulos_respuesta == "done":
            print " Hola que hace"
#            guardar_articulo()
#            print "hola que hace2"
            break
        else:
            print "ingrese otro articulo"



def menu():
    """Main menu"""
    print " "
    print "          Welcome"
    print " "
    print "     Menu"
    print " "
    print "  1. Add an item: "
    print "  2. Sell ARTICULOS: "
    print "  3. Exit. "
    print " "
    while True:
        respuesta = raw_input("Enter the number of your choice: ")
        if respuesta == "1":
            funciones_agregar_item()
            break #Esto es para que me corte el programa cuando la funcion es true"
        elif respuesta == "2":
            print "Sell ARTICULOS"
            vender_articulos()
            break
        elif respuesta == "3":
            print "Exit"
            break
        else:
            print "Insert a number of 1 of 3"

menu()
