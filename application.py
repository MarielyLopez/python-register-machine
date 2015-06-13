"""Register - Machine"""
#coding:utf-8
import os
import sys

PRECIO_ARTICULOS = {}
ARTICULOS_EXISTENCIA = {}

def agregar_articulo():
    limpiar_pantalla()
    print "Añade el nombre del articulo"
    nombre_articulo = raw_input("    >")
    return nombre_articulo.lower()


def agregar_precio():
    print "Ingresa el precio por unidad del articulo"
    while True:
        precio_articulo = raw_input("    >")
        try:
            precio_articulo = float(precio_articulo)
            return precio_articulo
        except:
            print "Ingresa un numero"


def agregar_numero_articulos():
    print "Ingresa la cantidad de articulos."
    while True:
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
    while True:
        respuesta_usuario = raw_input(" Quieres agregar más articulos? y/n ")
        respuesta_usuario = respuesta_usuario.lower()
        if respuesta_usuario == "y" or respuesta_usuario == "yes":
            return True
        elif respuesta_usuario == "n" or respuesta_usuario == "no":
            return False
        else:
            print "Ingresa una opcion valida"

def articulo_para_vender():
    print " ------Caja-----"
    articulo = raw_input("    > ")
    return articulo

def verificar_si_existe(articulo):
    existe = ARTICULOS_EXISTENCIA.has_key(articulo)
    print existe
    return existe

def verificar_cantidad(articulo):
    cantidad = ARTICULOS_EXISTENCIA.get(articulo)
    if cantidad > 0:
        print cantidad
        return True
    else:
        return False

def funciones_agregar_item():
    agregar_articulos = True
    while agregar_articulos == True:
        articulo = agregar_articulo()
        precio = agregar_precio()
        cantidad = agregar_numero_articulos()
        guardar_articulos(articulo, precio, cantidad)
        print PRECIO_ARTICULOS
        print ARTICULOS_EXISTENCIA
        agregar_articulos = agregar_mas_articulos()


def funciones_vender():
    articulo = articulo_para_vender()
    existe = verificar_si_existe(articulo)
    disponible = verificar_cantidad(articulo)

def limpiar_pantalla():
    sistema_operativo = os.name

    if sistema_operativo == "posix":
        os.system("reset")
    elif sistema_operativo == "nt":
        os.system("cls")


def menu():
    limpiar_pantalla()
    print ""
    print "  --------------Menu---------------"
    print "     Elige una opcion"
    print "     Ingresa 1 para agregar articulos"
    print "     Ingresa 2 para vender articulos"
    print "     Ingresa 3 para salir"
    print ""

    while True:
        ingresar_respuesta = raw_input("    > ")
        if ingresar_respuesta == "1":
            funciones_agregar_item()
        elif ingresar_respuesta == "2":
            funciones_vender()
        elif ingresar_respuesta == "3":
            print "Adios"
            break
        else:
            print "opcion invalida"
            break


menu()