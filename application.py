"""Register Machine"""
ARTICLES = {'Manzana':1.25, 'Pera':2.00, 'Sandia':10, 'Naranja':2.00}
ENTER_ARTICLES = {}

def card_gold():
    while True:
        print " "
        print "Do you have a card  Gold or silver?"
        print " "
        answer_card = raw_input("Insert the color of your card: ")
        if answer_card == "gold":
            print " Su descuento es de %5 en su factura."
            break
        elif answer_card == "silver":
            print "Su descuento es de %2 en su factura."
            break 
        elif answer_card == "silver and gold" or answer_card == "gold and silver":
            print " Su descuento es de %5 en su factura"
            break
        else:
            print "Ingrese Gold o Silver."

#while True:
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
    while True:
        print " "
        print "          Welcome"
        print " "
        print "     Menu"
        print " "
        print "  1. Add an item: "
        print "  2. Sell ARTICLES: "
        print "  3. Exit. "
        print " "
        answer = raw_input("Enter the number of your choice: ")
        if answer == "1":
            answer_y_n()
            #Esto es para que me corte el programa cuando la funcion es true"
        elif answer == "2":
            print "Sell ARTICLES"
            break
        elif answer == "3":
            print "Exit"
            break
        else:
            print "Insert a number of 1 of 3"

menu()
