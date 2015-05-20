"""Register Machine"""
def answer_y_n():
            add_answer = raw_input("Add a item: ")
            add_answer = add_answer.lower()
            add_price = raw_input("Price: ")
            print "Do you want to insert another article?"
            while True:
                add_answer1 = raw_input("y/n: ")
                if add_answer1 == "y":
                    item()
                    break
                elif add_answer1 == "n":
                    print "no"
                    break
                else:
                    print "Invalyd Option, insert y or n"

def menu():
    print " "
    print "    Menu"
    print " "
    print "  1. Add an item: "
    print "  2. Sell Articles: "
    print "  3. Exit. "
    item()

def item():
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
