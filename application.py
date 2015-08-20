"""registermachine"""
#coding:utf-8

import os
import sys

PRICE_ARTICLE = {}#Dictionari
EXISTENCE_ARTICLE = {}
PRODUCTS_PURCHASED = []#List
PRODUCTS_PURCHASED_NAMES = []
COUNTING_PRODUCTS = 0
COLORS_OF_CARDS = []
SORT_COLOR = []
SORT_OF_DISCOUNT = ""

def add_article():
    """It will ask the user to enter an article."""
    clear()
    print "It adds the name of the article"
    name_article = raw_input("     >")#The article inserted will be saving in variable name_article.
    return name_article.lower()

def add_price():
    """It will ask the user to enter price of article"""
    print "Inserts the item's price"
    addprice = True
    while addprice == True:
        price_article = raw_input("    >")
        try:
            price_article = float(price_article)
            return price_article
        except ValueError:
            print "Insert a number."

def add_quantity_items():
    """It will ask the user to enter quantity of articles of there's at inventory."""
    print "Inserts add quantity of items."
    addquantityitems = True
    while addquantityitems == True:
        quantity = raw_input("    >")
        try:
            quantity = int(quantity)
            return quantity
        except ValueError:
            print "Try again,enter a integer for inventory"

def save_articles(article, price, quantity):
    """will be saving price of article in the dictionary."""
    PRICE_ARTICLE[article] = price
    EXISTENCE_ARTICLE[article] = quantity

def add_more_article():
    """This will ask the user to enter an article."""
    addmorearticle = True
    while addmorearticle == True:
        user_answer = raw_input(" Are you want to add more articles? y/n  ")
        user_answer = user_answer.lower()
        if user_answer == "y" or user_answer == "yes":
            return True
        elif user_answer == "n" or user_answer == "no":
            menu()
            return False
        else:
            print "Insert a valid option"

#start the fuctions for done.
def article_to_sell():
    """There will be enter all products sold."""
    print " "
    print " --------------Cash---------------"
    print "  "
    article = raw_input("    > ")
    article = article.lower()
    return article

def check_if_exists(article):
    """There will be check if exists article and then take key"""
    exists = EXISTENCE_ARTICLE.has_key(article)
    return exists

def check_quantity(article):
    """There will be check quantity the numbers of names repeared"""
    quantity = EXISTENCE_ARTICLE.get(article)
    print "Had " + str(quantity), article, "(s)"
    if quantity > 0:
        EXISTENCE_ARTICLE[article] = quantity -1
        count_products_name(article)
        print "There is", EXISTENCE_ARTICLE.get(article), article
    else:
        print "Not available"

def count_products_name(article):
    """There will be count names of articles"""
    PRODUCTS_PURCHASED_NAMES.append(article)

def order_products():
    """It will display the products in alphabetical order"""
    PRODUCTS_PURCHASED = sorted(PRODUCTS_PURCHASED_NAMES)# It will alphabetical order.
    counting_products = len(PRODUCTS_PURCHASED)#count how many here.
    #here they are numbered and ordered products are stored.
    creation_of_invoice(counting_products, PRODUCTS_PURCHASED)
    return False

def check_of_done(article):
    """this only will be to verified word DONE"""
    if article == "done":
        print "Card has been inserting."
        print "It will print the invoice"
        print "-----------------------------------------"
        return True
    #        SORT_OF_DISCOUNT = "gold"
        return"gold"
    elif article == "silver":
    #        SORT_OF_DISCOUNT = "silver"
        return "silver"
    elif article == "gold":
    #        SORT_OF_DISCOUNT = "gold"
        return "gold"
    else:
        return False

def creation_of_invoice(recibir_conteo, lista):
    """This only will be print my invoice before to create"""
    clear()
    subtotal = 0
    subtotal_with_iva = 0
    final_total = 0
    print "  "
    print "----------------INVOICE------------------"
    print "  "
    print "Your quantity of purchased article is: " + str(recibir_conteo)
    print "Card inserted:", print_card()
    print "  "
    print "Quantity.        Product           Price/Unit"
    print "  "
    for product in PRICE_ARTICLE:
        counting_products = lista.count(product)
        if counting_products > 0:
            price = PRICE_ARTICLE[product]
            subtotal += (counting_products*price)
            subtotal_with_iva = (subtotal* 0.12)+subtotal
            final_total = subtotal_with_iva - discounting_of_card(subtotal)
            print counting_products, "                ", product +": ", "Q.%.2f" % price +" unit"
    print "subtotal                 ..............", "Q.%.2f" % subtotal
    print "Discount is              ..............", "Q.%.2f" % discounting_of_card(subtotal)
    print "Subtotal with iva        ..............", "Q.%.2f" % subtotal_with_iva
    print "Final Total              ..............", "Q.%.2f" % final_total
    print "-----------------------------------------------"
    print "           Thank you for shopping with us."
    print " "
    print "Press enter"
    raw_input(" ")
    delete_data()
    menu()
#    new_purchase()

def delete_data():
    """this may only allow a new purchase"""
    PRICE_ARTICLE = {}#Dictionari
    EXISTENCE_ARTICLE = {}
    del PRODUCTS_PURCHASED[0:]#List
    del PRODUCTS_PURCHASED_NAMES[0:]
    COUNTING_PRODUCTS = 0
    del COLORS_OF_CARDS[0:]
    del SORT_COLOR[0:]
    SORT_OF_DISCOUNT = ""

def clear():
    """Cleans the data on screen."""
    if os.name == "posix":
        os.system("reset")
    elif os.name == ("nt"):
        os.system("cls")

def print_card():
    """This check color of cards."""
    simbol_gold = "G"
    simbol_silver = "S"
    gold = 0
    silver = 0
    gold_and_silver = 0
    if simbol_gold in SORT_COLOR:
        gold += 1
    if simbol_silver in SORT_COLOR:
        silver += 1
    if gold > 0 and silver == 0:
        return "Gold"
    elif silver > 0 and gold == 0:
        return "Silver"
    if silver > 0 and gold > 0:
        return "Gold"
    else:
        return 0

def discounting_of_card(subtotal):
    """The discount is selected depending of inserted by the user."""
    simbol_gold = "G"
    simbol_silver = "S"
    gold = 0
    silver = 0
    gold_and_silver = 0
    if simbol_gold in SORT_COLOR:
        gold += 1
    if simbol_silver in SORT_COLOR:
        silver += 1
    if gold > 0 and silver == 0:
        return subtotal*0.05
    elif silver > 0 and gold == 0:
        return subtotal*0.02
    elif silver > 0 and gold > 0:
        return subtotal*0.05
    else:
        return 0

def fuctions_add_items():
    """this only show the variables, later will be call in menu"""
    add_articles = True
    while add_articles == True:
        article = add_article()
        price = add_price()
        quantity = add_quantity_items()
        save_articles(article, price, quantity)
        add_articles_ask = add_more_article()

def fuctions_sell():
    """This only check if the user has entered siler or gold for later to sell"""
    sell_products = True
    while sell_products == True:
        article = article_to_sell()
        if check_of_done(article) == True:
            sell_products = order_products()
        elif check_of_done(article) == "silver":
            print "It's inserted Silver"
            SORT_COLOR.append("S")
        elif check_of_done(article) == "gold":
            print "It's inserted Gold"
            SORT_COLOR.append("G")
        else:
            if check_if_exists(article) == True:
                check_quantity(article)
            else:
                print"The product doesn't exists"

def menu():
    """Print my menu asking the user to input your choice."""
    clear()
    print ""
    print " --------------Menu---------------"
    print "     Choose an option"
    print "     Enter 1 to add articles"
    print "     Enter 2 for sell articles"
    print "     Enter 3 to exit"
    print ""
    answermenu = True
    while answermenu == True:
        insert_answer = raw_input("    > ")
        if insert_answer == "1":
            fuctions_add_items()
        elif insert_answer == "2":
            fuctions_sell()
            break
        elif insert_answer == "3":
            print "Good bye"
            sys.exit(1)
        else:
            print "Invalid option"

menu()
