#coding:utf8
"""Register Machine"""
ARTICLES = {'Manzana':2.00, 'Pera':2.00, 'Sandia':10, 'Naranja':2.00, 'Fresa':5.00,
            'Mango':3.00, 'Banano':1.00, 'Melon':5, 'Piña':5,}
ENTER_ARTICLES = {}

def card_gold():
#this function will ask if that have a card gold or a card silver."""
    while True:
        print " "
        print "Do you have a card  Gold or silver?"
        print " "
        answer_card = raw_input("Insert the color of your card: ")
        print " "
        answer_card = answer_card.lower()
        if answer_card == "gold":
            print " Su descuento es de %5 en su factura."
            print " "
            break
        elif answer_card == "silver":
            print "Su descuento es de %2 en su factura."
            print " "
            break
        elif answer_card == "silver and gold" or answer_card == "gold and silver":
            print " Su descuento es de %5 en su factura"
            print " "
            break
        else:
            print "Ingrese Gold o Silver."

# Insert a article
def answer_y_n():
    while True:
        """Pedira al ususario ingresar un articulo."""
        add_answer = raw_input("Add an item: ")
        add_answer = add_answer.lower()
        if add_answer == "done":
            print " "
            print "             Sell Articles"
            card_gold()
            break
        else:
            add_price = raw_input("Price: ")
#_price es el resultado de  funcionENTER_ARTICLEStieneelproductoingresadoelususarioes "add_ARTICLES"
            ENTER_ARTICLES[add_answer] = add_price

def article_new():
    while True:
        add_answer1 = raw_input("create new item y/n: ")
        if add_answer1 == "y":
            print " "
            answer_y_n()
        elif add_answer1 == "n":
            print " "
            break
        else:
            print "Invalyd Option, insert y or n"

def menu():
    """Main menu"""
    print " "
    print "                 Welcome"
    print " "
    print "     Menu"
    print " "
    print "  1. Add an item: "
    print "  2. Sell ARTICLES: "
    print "  3. Exit. "
    print " "
    while True:
        answer = raw_input("Enter the number of your choice: ")
        print " "
        if answer == "1":
            answer_y_n()
            break
        elif answer == "2":
            print "Sell ARTICLES"
            break
        elif answer == "3":
            print "Exit"
            break
        else:
            print "Insert a number of 1 of 3"

menu()
