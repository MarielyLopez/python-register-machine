"""Register Machine"""
articles = {'Manzana':1.25, 'Pera':2.00,'Sandia':10,'Naranja':2.00,}
enter_articles = {}
def answer_y_n():
            add_answer = raw_input("Add an item: ")
            add_answer = add_answer.lower()
            add_price = raw_input("Price: ")
            enter_articles[add_answer] = add_price #"add_price" es el resultado de la funcion "enter_articles" que tiene como parametro el producto ingresado por el ususario que es "add_articles"
            print enter_articles
            print "Do you want to insert another article?"
            article_new()

def article_new():
    while True:
        add_answer1 = raw_input("y/n: ")
        if add_answer1 == "y":
            print " "
            answer_y_n()
            break
        elif add_answer1 == "n":
            print " "
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
    print "  2. Sell Articles: "
    print "  3. Exit. "
    print " "
    while True:
        answer = raw_input("Enter the number of your choice: ")
        if answer == "1":
            answer_y_n()
            break #Esto es para que me corte el programa cuando la funcion es true"
        elif answer == "2":
            print "Sell Articles"
            break
        elif answer == "3":
            print "Exit"
            break
        else:
            print "Insert a number of 1 of 3"

menu()
