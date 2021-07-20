"""Hangman created May 16th 
   I need to control for case sentence words and no numbers
"""
letra = '' 
import random,sys,re,os
import pyinputplus as pyip
os.system('clear')
false_count = 1
xword=[]
guessed_letras = [] 
import time
correct_word = []
inFile = open("word_list", "r")
line = inFile.readlines()
xrandom = (random.choice(list(open('word_list'))))
xrandom = xrandom.rstrip('\r\n') #this line is to remove line feed
original_word = xrandom

guess_count = 6 
count_remaining = 6 

while guess_count > 0: 
    guessed_letras.append(letra) 
    letra = pyip.inputStr('Type in a lower case letter ').lower()
    if letra in guessed_letras:
        already_guessed = set(guessed_letras)
        print(f'you already guessed the letter',' '.join(already_guessed))
        continue

    else:
        """compares the letter guess with the generated random word"""
        hangRegex = re.compile(letra) #letra is the word that is inputted. 
        xword = hangRegex.findall(xrandom)
        if xword and xword not in guessed_letras: 
            print('correct!')
            for i in xword:
                new_word = xrandom.split(i) #this removes the letter that is guessed
                new_word2 = (''.join(new_word)) 
                print('what is new_word2 ',new_word2)
                correct_word.append(xword)        # this begans to rebuild the orginal word
                xrandom = new_word2
                guess_count = guess_count + 1
                if new_word2 == "" or correct_word == original_word:
                     #print('original_word ', original_word)
                     print(f"\tcongrats! You win the word was {original_word}")  
                     sys.exit()
        else:
           count_remaining = count_remaining - 1 
           print(f'wrong, you have {count_remaining} chance(s) left') 
           if count_remaining == 0:
               print(f"\tyou lose, the word was", original_word)
               sys.exit() 

