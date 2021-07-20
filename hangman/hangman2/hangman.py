"""Hangman created May 16th 
   I need to control for case sentence words and no numbers
"""

constri_count = 1
import random,sys,re,os
import pyinputplus as pyip
os.system('clear')
#hangRegex = re.compile(r'(a-zA-Z]+)')

def constri_word(): 
    """this will create a random word from a text file in current directory called word_list"""
    inFile = open("word_list", "r")
    line = inFile.readlines()
    constri_word.xrandom = (random.choice(list(open('word_list'))))
    constri_word.xrandom = constri_word.xrandom.rstrip('\r\n') #this line is to remove line feed

def constri_exp():  
    while new_word2:
        letra = pyip.inputStr('Type in a letter ')
        """compares the letter guess with the generated random word"""
        global constri_count
        constri_count = len(constri_word.xrandom) #gets the length of the word and use it to count backwards.  
        hangRegex = re.compile(letra) #letra is the word that is inputted. 
        x = hangRegex.findall(constri_word.xrandom)
        #print(x)
        for i in x:
            new_word = constri_word.xrandom.split(i) #this removes the letter that is guessed
            new_word2 = (''.join(new_word)) 
            print(new_word2)

constri_word()
constri_exp()

