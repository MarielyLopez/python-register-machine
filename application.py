"""Register Machine"""

def menu():
    print " "
    print "    Menu"
    print " "
    print "  1. Add an item: "
    print "  2. Sell Articles: "
    print "  3. Exit. "
    while True:
        answer = raw_input("Enter the number of your choice: ")
        if answer == "1":
            print "Add an item"
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
