"""registermachine"""
#coding:utf-8
from operator import itemgetter
import os
import sys

PRECIO_ARTICULOS = {}
ARTICULOS_EXISTENCIA = {}
PRODUCTOS_COMPRADOS = []
PRODUCTOS_COMPRADOS_NOMBRES = []
CONTEO_PRODUCTOS = 0
COLOR_DE_TARJETAS = []
tipo_de_color=[]
TIPO_DE_DESCUENTO = ""

def agregar_articulo():
    limpiar_pantalla()
    print "Añade el nombre del articulo"
    nombre_articulo = raw_input("     >")
    return nombre_articulo.lower()


def agregar_precio():
    print "Ingresa el precio por unidad del articulo"
    agregarprecio = True
    while agregarprecio == True:
        precio_articulo = raw_input("    >")
        try:
            precio_articulo = float(precio_articulo)
            return precio_articulo
        except:
            print "Ingresa un numero"


def agregar_numero_articulos():
    print "Ingresa la cantidad de articulos."
    agregarnumeroarticulos = True
    while agregarnumeroarticulos == True:
        cantidad = raw_input("    >")
        try:
            cantidad = int(cantidad)
            return cantidad
        except:
            print "Ingresa un numero"


def guardar_articulos(articulo, precio, cantidad):
    PRECIO_ARTICULOS[articulo] = precio
    ARTICULOS_EXISTENCIA[articulo] = cantidad

def agregar_mas_articulos():
    agregarmasarticulos = True
    while agregarmasarticulos == True:
        respuesta_usuario = raw_input(" Quieres agregar más articulos? y/n ")
        respuesta_usuario = respuesta_usuario.lower()
        if respuesta_usuario == "y" or respuesta_usuario == "yes":
            return True
        elif respuesta_usuario == "n" or respuesta_usuario == "no":
            menu()
            return False
        else:
            print "Ingresa una opcion valida"

#start the fuctions for done.
def articulo_para_vender():
    print " "
    print " --------------Caja---------------"
    print "  "
    articulo = raw_input("    > ")
    articulo = articulo.lower()
    return articulo

def verificar_si_existe(articulo):
    existe = ARTICULOS_EXISTENCIA.has_key(articulo)
    return existe

def verificar_cantidad(articulo):
    cantidad = ARTICULOS_EXISTENCIA.get(articulo)
    print "Habia " + str(cantidad), articulo, "(s)"
    if cantidad > 0:
        ARTICULOS_EXISTENCIA[articulo] = cantidad -1
        conteo_de_productos_nombres(articulo)
        print "Hay", ARTICULOS_EXISTENCIA.get(articulo), articulo
        limpiar_pantalla()
    else:
        print "No disponible"


def conteo_de_productos_nombres(articulo):
    PRODUCTOS_COMPRADOS_NOMBRES.append(articulo)

def orden_productos():
    PRODUCTOS_COMPRADOS = sorted(PRODUCTOS_COMPRADOS_NOMBRES)
    CONTEO_PRODUCTOS = len(PRODUCTOS_COMPRADOS)
    creacion_de_factura(CONTEO_PRODUCTOS, PRODUCTOS_COMPRADOS)
    return False

def verificacion_de_done(articulo):
        if articulo == "done":
            print "TARJETA INGRESADA"
            print "Se Imprimira la factura"
            print "-----------------------------------------"
            return True
            TIPO_DE_DESCUENTO = "gold"
            return"gold"
        elif articulo == "silver":
            TIPO_DE_DESCUENTO = "silver"
            return "silver"
        elif articulo == "gold":
            TIPO_DE_DESCUENTO = "gold"
            return "gold"
        else:
            return False


def creacion_de_factura(recibir_conteo, lista):
    limpiar_pantalla()
    subtotal = 0
    print "  "
    print "----------------FACTURA------------------"
    print "  "
    print  "Su Cantidad de productos comprados es: " + str(recibir_conteo)
    print "  "
    print "Cant.        PRODUCTO           Precio/unidad"
    print "  "
    for producto in PRECIO_ARTICULOS:
        CONTEO_PRODUCTOS = lista.count(producto)
        if CONTEO_PRODUCTOS > 0:
            precio = PRECIO_ARTICULOS[producto]
            subtotal += (CONTEO_PRODUCTOS*precio)
            subtotal_con_iva = (subtotal* 0.12)+subtotal
            Total_final = subtotal + descontando_descuentos(subtotal)
            print CONTEO_PRODUCTOS, producto +"   ...........................", str(precio) +" cada uno(a)"
    print "Total sin descuento   ..............", subtotal
    print "Total con iva         ..............",subtotal_con_iva
    print "Total con Final       ..............", Total_final
    print "-------------------------------------------"
    print "           Gracias por su compra"
    print " "
    sys.exit(1)

def descontando_descuentos(subtotal):
# se selecciona el descuento dependiendo de lo ingresao por el usuario
    simbol_gold = "G"
    simbol_silver = "S"
    gold = 0
    silver = 0
    gold_and_silver = 0
    if simbol_gold in tipo_de_color:
        gold +=1
    if simbol_silver in tipo_de_color:
        silver +=1
    if gold >0 and silver == 0:
        return subtotal*0.05
    elif silver >0 and gold == 0:
        return subtotal*0.02
    if silver >0 and gold >0:
        return subtotal*0.05
    else:
        return "0"

def funciones_agregar_item():
    agregar_articulos = True
    while agregar_articulos == True:
        articulo = agregar_articulo()
        precio = agregar_precio()
        cantidad = agregar_numero_articulos()
        guardar_articulos(articulo, precio, cantidad)
        agregar_articulos_pregunta = agregar_mas_articulos()


def funciones_vender():
    vender_productos = True
    while vender_productos == True:
        articulo = articulo_para_vender()
        if verificacion_de_done(articulo) == True:
            vender_productos = orden_productos()
        elif verificacion_de_done(articulo) == "silver":
            print "SE INGRESO SILVER"
            tipo_de_color.append("S")
        elif verificacion_de_done(articulo) == "gold":
            print "SE INGRESO GOLD"
            tipo_de_color.append("G")
        else:
            if verificar_si_existe(articulo) == True:
                disponible = verificar_cantidad(articulo)
                if disponible == False:
                    print "No disponible"
                    vender_productos = True
            else:
                print "Articulo no existe"

def limpiar_pantalla():
    sistema_operativo = os.name
    if sistema_operativo == "posix":
        os.system("reset")
    elif sistema_operativo == "nt":
        os.system("cls")

"""Imprimira mi menu pidiendole al usuario ingresar su opcion."""
def menu():
    limpiar_pantalla()
    print ""
    print " --------------Menu---------------"
    print "     Elige una opcion"
    print "     Ingresa 1 para agregar articulos"
    print "     Ingresa 2 para vender articulos"
    print "     Ingresa 3 para salir"
    print ""
    respuestamenu = True
    while respuestamenu == True:
        ingresar_respuesta = raw_input("    > ")
        if ingresar_respuesta == "1":
            funciones_agregar_item()
        elif ingresar_respuesta == "2":
            funciones_vender()
            verificar_cantidad
            break
        elif ingresar_respuesta == "3":
            print "Adios"
            sys.exit(1)
        else:
            print "opcion invalida"
menu()
