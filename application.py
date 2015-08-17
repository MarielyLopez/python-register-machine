"""registermachine"""
#coding:utf-8
from operator import itemgetter
import os
import sys

PRICE_ARTICLE = {}#Dictionari
EXISTENCE_ARTICLE = {}
PRODUCTS_PURCHASED = []#List
PRODUCTS_PURCHASED_NAMES = []
COUNT_PRODUCTS = 0
COLORS_OF_CARDS = []
SORT_COLOR = []
SORT_OF_DISCOUNT = ""

def add_article():
#It will ask the user to enter an article.
    resert_window()
    print "It adds the name of the article"
    name_article = raw_input("     >")#The article inserted will be saving in variable name_article.
    return name_article.lower()


def add_price():
#It will ask the user to enter price of article
    print "Inserts the item's price"
    addprice = True
    while addprice == True:
        price_article = raw_input("    >")
        try:
            price_article = float(price_article)
            return price_article
        except:
            print "Insert a number ."


def add_quantity_items():
#It will ask the user to enter quantity of articles of there's at inventory.
    print "Inserts add quantity of items."
    addquantityitems = True
    while addquantityitems == True:
        quantity = raw_input("    >")
        try:
            quantity = int(quantity)
            return quantity
        except:
            print "Try again,enter a integer for inventory"


def save_articles(article, price, quantity):
#will be saving price of article in the dictionary.
    PRICE_ARTICLE[article] = price
    EXISTENCE_ARTICLE[article] = quantity

def add_more_article():
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
#There will be enter all products sold.
    print " "
    print " --------------Cash---------------"
    print "  "
    article = raw_input("    > ")
    article = article.lower()
    return article

def check_if_exists(article):
    exists = EXISTENCE_ARTICLE.has_key(article)
    return exists

def check_quantity(article):
    quantity = EXISTENCE_ARTICLE.get(article)
    print "Had " + str(quantity), article, "(s)"
    if quantity > 0:
        EXISTENCE_ARTICLE[article] = quantity -1
        count_products_name(article)
        print "There is", EXISTENCE_ARTICLE.get(article), article
    else:
        print "Not available"


def count_products_name(article):
    PRODUCTS_PURCHASED_NAMES.append(article)

def order_products():
    #It will display the products in alphabetical order
    PRODUCTS_PURCHASED = sorted(PRODUCTS_PURCHASED_NAMES)# It will alphabetical order.
    COUNT_PRODUCTS = len(PRODUCTS_PURCHASED)#count how many here.
#here they are numbered and ordered products are stored.
    Creation_of_invoice(COUNT_PRODUCTS, PRODUCTS_PURCHASED)
    return False

def check_of_done(article):
    if article == "done":
        print "Card has been inserting."
        print "It will print the invoice"
        print "-----------------------------------------"
        return True
        SORT_OF_DISCOUNT = "gold"
        return"gold"
    elif article == "silver":
        SORT_OF_DISCOUNT = "silver"
        return "silver"
    elif article == "gold":
        SORT_OF_DISCOUNT = "gold"
        return "gold"
    else:
        return False


def Creation_of_invoice(recibir_conteo, lista):
    resert_window()
    subtotal = 0
    print "  "
    print "----------------INVOICE------------------"
    print "  "
    print "Your quantity of purchased article is: " + str(recibir_conteo)
    print "Card inserted:" , print_card()
    print "  "
    print "Quantity.        Product           Price/Unit"
    print "  "
    for product in PRICE_ARTICLE:
        COUNT_PRODUCTS = lista.count(product)
        if COUNT_PRODUCTS > 0:
            price = PRICE_ARTICLE[product]
            subtotal += (COUNT_PRODUCTS*price)
            subtotal_with_iva = (subtotal* 0.12)+subtotal
            Total_final = subtotal_with_iva - discounting_of_card(subtotal)
            print COUNT_PRODUCTS,product +"  ...........................","Q.%.2f" % price +"each."
    print "Undiscounted total    ..............","Q.%.2f" % subtotal
    print "Undiscounted is       ..............","Q.%.2f" % discounting_of_card(subtotal)
    print "Total with iva        ..............","Q.%.2f" % subtotal_with_iva
    print "Total Final           ..............","Q.%.2f" % Total_final
    print "-----------------------------------------------"
    print "           Thank you for shopping with us."
    print " "
    sys.exit(1)

def print_card():
#This check color of cards.
    simbol_gold = "G"
    simbol_silver = "S"
    gold = 0
    silver = 0
    gold_and_silver = 0
    if simbol_gold in SORT_COLOR:
        gold +=1
    if simbol_silver in SORT_COLOR:
        silver +=1
    if gold >0 and silver == 0:
        return "Gold"
    elif silver >0 and gold == 0:
        return "Silver"
    if silver >0 and gold >0:
        return "Gold"
    else:
        return 0

def discounting_of_card(subtotal):
# The discount is selected depending of inserted by the user.
    simbol_gold = "G"
    simbol_silver = "S"
    gold = 0
    silver = 0
    gold_and_silver = 0
    if simbol_gold in SORT_COLOR:
        gold +=1
    if simbol_silver in SORT_COLOR:
        silver +=1
    if gold >0 and silver == 0:
        return subtotal*0.05
    elif silver >0 and gold == 0:
        return subtotal*0.02
    elif silver >0 and gold >0:
        return subtotal*0.05
    else:
        return 0

def fuctions_add_items():
    add_articles = True
    while add_articles == True:
        article = add_article()
        price = add_price()
        quantity = add_quantity_items()
        save_articles(article, price, quantity)
        add_articles_ask = add_more_article()


def fuctions_sell():
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
#        elif check_of_done(article) != "gold" and check_of_done(article) != "silver" and check_of_done (article) != "gold" and :
#            print "It's not has been inserting cards"
        else:
            if check_if_exists(article) == True:
                available = check_quantity(article)
                if available == False:
                    print "No available"
                    sell_products = True
            else:
                print "The article not exists."

def resert_window():
    system_operative = os.name
    if system_operative == "posix":
        os.system("reset")
    elif system_operative == "nt":
        os.system("cls")

#Print my menu asking the user to input your choice.
def menu():
    resert_window()
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
            check_quantity
            break
        elif insert_answer == "3":
            print "Good bye"
            sys.exit(1)
        else:
            print "Invalid option"
menu()
