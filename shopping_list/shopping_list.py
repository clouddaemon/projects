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
item_line = ''
itim = []
def sua_choices():
    print('1.   View shopping list')
    print('2.   Add item to shopping list')
    print('3.   Remove item from shopping list')
    print('4.   Check if item is on shopping list')
    print('5.   Clear shopping list')
    print('6.   Exit')


def view_items():
    if file.exists():    
        f=open("shopping_list.txt", "r")
        print("here's your items ")
        for i in (f.readlines()):
            item_line = i.rstrip()
            print(item_line)
            time.sleep(1) 
        f.close()
    else:
        print("The shopping list does not exist. Add something \n")
        
def add_items():
    filecontents = input('What would you like to add to your list? ')    
    if file.exists():
        f=open("shopping_list.txt", "a")
    else:
        f=open("shopping_list.txt", "w")
    f.write(filecontents)
    f.write('\n')
    f.close() 

def remove_item():
    #################################################################################################################
    # -read- creates a string. Treats each character separately                                                     #  
    # -readline- creates a string. Reads a single line of the file                                                  # 
    # -for- creates a string to be interated over                                                                   #
    # -readlines- creates a list  of all the files. has no string function                                          #
    #################################################################################################################
    remove_items = input("which item do you want to remove from shopping list? ")
 ##Open a file to read with open("file", "r"). Use file.readlines() to create a list where each element is a line from the file. Close the file.####

    f=open("shopping_list.txt", "r+") 
    foods = (f.readlines())
    f.close() 

 #Open the file again to write with open("file", "w"). Use a for-loop to iterate through the list of lines#    
    f2=open("shopping_list.txt","w+") 
    for i in foods:
        if i.strip("\n") !=remove_items:
            f2.write(i)
    f.close()       
 
  
def check_items():
    search_items = input("what Item do you want to search for? ")
    f=open("shopping_list.txt", "r")
    for i in (f.readlines()):
        item_line = i.rstrip() 
        if search_items == item_line:
            print(f"{item_line} is already on the shoppping list")
            time.sleep(1)
            break
        else:
            print(f"{search_items} Items not found on list")
            print ('\n')
    f.close()

def clear_list():
    certo = input ("Are you sure you want to remove all items from shopping list?  type 'YES' to confirm ")
    if certo == "YES":
        os.remove("shopping_list.txt")


#############################this is the choice section########################
while response != 6:
    sua_choices()

    response = pyip.inputNum()
    os.system('clear') 
    if response == 1:
        view_items()

    if response == 2:
        add_items()

    if response == 3:
        remove_item()

    if response == 4:
        check_items()

    if response == 5:
        clear_list()

    if response == 6:
        print("I am exiting... ")
        sys.exit()
