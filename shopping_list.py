#! python3.9
################################################################################
#                   Project shopping list                                       #
#                         4/30/2021                                             #
#################################################################################
import os, sys, time
import pyinputplus as pyip
os.system('clear')
import pathlib
response = 0
certo = "no"
file = pathlib.Path("shopping_list.txt")

def sua_choices():
    print('1.   View shopping list')
    print('2.   Add item to shopping list')
    print('3.   Remove item from shopping list')
    print('4.   Check if item is on shopping list')
    print('5.   How many items on shopping list')
    print('6.   Clear shopping list')
    print('7.   Exit')


def view_items():
    if file.exists():    
        f=open("shopping_list.txt", "r")
        print(f.readlines()) 
        f.close()
    else:
        print("The shopping list does not exist. Add something \n")
        
def add_items():
    filecontents = input('What would you like to add to your list? ')    
    #file = pathlib.Path("shopping_list.txt")

    if file.exists():
        f=open("shopping_list.txt", "a")
    else:
        f=open("shopping_list.txt", "w")

    f.write(filecontents)
    f.write('\n')
    f.close() 

def remove_items():
    certo = input ("Are you sure you want to remove all items from shopping list?  type 'YES' to confirm ")
    if certo == "YES":
        os.remove("shopping_list.txt")
 
def check_items():
    search_items = input("what Item do you want to search for? ")
    f=open("shopping_list.txt", "r")
    for i in (f.readlines()):
        item_line = i.rstrip() 
        if search_items == item_line:
            print(f"{item_line} is already on the shoppping list")
            time.sleep(2)
            break
        else:
            print(f"{search_items} Items not found on list")
            print ('\n')
    f.close()


def howmany_items():
    pass

def clear_list():
    pass


while response != 7:
    sua_choices()

    response = pyip.inputNum()
    os.system('clear') 
    if response == 1:
        view_items()

    if response == 2:
        add_items()

    if response == 3:
        remove_items()

    if response == 4:
        check_items()

    if response == 5:
        howmany_items()

    if response == 6:
        clear_list()

    if response == 7:
        print("I am exiting... ")
        sys.exit()
