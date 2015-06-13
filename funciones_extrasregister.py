def to_lower(word):
	word = word.lower()
	return word


#coding:utf8
"""Register Machine"""
import string
ARTICLES = {'Manzana':1.25, 'Pera':2.00, 'Sandia':10, 'Naranja':2.00,
            'Mango':3.00,'Banano':1.00, 'Melon':5, 'Piña':5,}
ENTER_ARTICLES = {}


#while True:
def answer_y_n():

    while True:
        """Pedira al ususario ingresar un articulo."""
        add_answer = raw_input("Add an item: ")
        add_answer = add_answer.lower()
        while True:
            try:
                add_price = float(raw_input("Price: "))
                article_new()
                #_price es el resultado de  funcionENTER_ARTICLEStieneelproductoingresadoelususarioes "add_ARTICLES"
                ENTER_ARTICLES[add_answer] = add_price
                articlenew(add_answer)
            except ValueError:
                print "Insert only numbers and floats."
                while True:
                    break
                    print ENTER_ARTICLES



def articlenew(add_answer):
    if add_answer == "done":
        print "Sell Articles"
        answer_articlenew = raw_input("Insert an item: ")
#        answer_y_n()
    else:
        print "Insert an item"
#        answer_y_n()

#print "Do you want to insert another article?"M
#article_new()

def article_new():
#verificara si la respuesta es no o si y ejecutara el programa sgun la condicion.
    while True:
        print "  Do you do insert a new article?"
        add_answer1 = raw_input("y/n: ")
        if add_answer1 == "y":
            print " "
            answer_y_n()
            break
        elif add_answer1 == "n":
            print " "
            menu()
            break
        else:
            print "Invalyd Option, insert y or n"

def menu():
    """Main menu"""
    print " "
    print "          Welcome"
    print " "
    print "     Menu"
    print " "
    print "  1. Add an item: "
    print "  2. Sell ARTICLES: "
    print "  3. Exit. "
    print " "
    valuemenu = True
    while valuemenu ==True:
        answer = raw_input("Enter the number of your choice: ")
        if answer == "1":
            answer_y_n()
            break #Esto es para que me corte el programa cuando la funcion es true"
        elif answer == "2":
            print "Sell ARTICLES"
            break
        elif answer == "3":
            print "Exit"
            valuemenu == False
            break

        else:
            print "Insert a number of 1 of 3"

menu()






#resgister 3
"""def tener_tarjeta():
    while True:
        print "Tiene tarjeta?"
        respuesta_tener_tarjeta = raw_input("si/no: ")
        if respuesta_tener_tarjeta == "si":
            print "Ingrese el color de su tarjeta por favor: "
            color_tarjeta()
            break
        elif respuesta_tener_tarjeta == "no":
            print "Necesita una tarjeta."
            break
        else:
            print "Ingrese una respuesta por favor."""


"""def color_tarjeta():
    print " "
    respuesta_color_tarjeta = raw_input("Ingrese el color de su tarjeta aqui: ")
    if respuesta_color_tarjeta == "gold":
        respuesta_color_tarjeta = respuesta_color_tarjeta.lower
        tarjeta_gold()
#        break
    elif respuesta_color_tarjeta == "silver":
        respuesta_color_tarjeta = respuesta_color_tarjeta.lower
        tarjeta_silver()
#        break
    elif respuesta_color_tarjeta == "gold y silver":
        respuesta_color_tarjeta = respuesta_color_tarjeta.lower
        tarjeta_gold()
#        break
    else:
        print "Ingrese un color por favor."""


"""def tarjeta_gold():
    print " "
    print "Ya que tienes una tarjeta Gold tu descuento es: "
    print " """

"""def tarjeta_silver():
    print " "
    print "Ya que tienes una tarjeta Silver tu descuento es :"
    print " """





# register e

def verificacion_inventario():
    for fruta in ARTICULOS:
        fruta = fruta.iterkeys()
        if fruta == ingresando_articulos():
            print fruta
#    for ingresando_articulos() in ARTICULOS
#    return ingresando_articulos()
#    print "ingresando_articulos"
