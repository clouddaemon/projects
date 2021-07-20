"""Hangman created May 16th 
   I need to control for case sentence words and no numbers
"""

constri_count = 1
import random,sys,re,os
import pyinputplus as pyip
os.system('clear')
guessed_letras = []
#guessed_letras = set() 
found_letra = []
won = False
def constri_word(): 
    """this will create a random word from a text file in current directory called word_list"""
    inFile = open("word_list", "r")
    line = inFile.readlines()
    constri_word.xrandom = (random.choice(list(open('word_list'))))
    constri_word.xrandom = constri_word.xrandom.rstrip('\r\n') #this line is to remove line feed

def constri_exp():  
    found_letras = [] 
    word_list = constri_word.xrandom 
    while constri_word.xrandom:
        word_list_dash = [letter if letter in guessed_letras else '_' for letter in word_list] 
        print('Current word: ', ' '.join(word_list_dash))
        letra = pyip.inputStr('Type in a letter ')
        if letra in guessed_letras:
            print('you already guessed that word ')
            continue
        hangRegex = re.compile(letra) #letra is the word that is inputted. 
        found_letras = hangRegex.findall(constri_word.xrandom)
        new_word = constri_word.xrandom.split(letra) #this removes the letter that is guessed
        guessed_letras.append(letra)
        new_word2 = (''.join(new_word))
        
        constri_word.xrandom = new_word2
        if new_word2 == "":
            print('word guessed!')
            won = True

        elif len(guessed_letras) == 6:
            os.system('clear')
            print('The word was ', word_list)
            sys.exit("you are out of guesses")
 
        elif letra in new_word2: 
             print('You guessed correctly')

      
    print('parabens!')
    response = pyip.inputYesNo('Would you like to play again?')
     

constri_word()
constri_exp()
