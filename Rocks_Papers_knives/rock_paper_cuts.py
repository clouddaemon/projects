""" Rock paper cut - you will be playing against the computer """
import random,sys,re,os
import pyinputplus as pyip
os.system('clear')
computer = 0
user = 0


play_again = 'Yes'
while play_again == 'Yes':
    print('\n')
    response = pyip.inputMenu(['rocks', 'paper', 'scissors'])
    letters =['paper','rocks','scissors']
    random_index = random.choice(letters)

    #print('computer picked ',random_index)
    if response == random_index:
        #print(f'the computer picked {random_index} so its a draw')
        print('you and the computer have both chosen {} Its a tie.'.format(random_index))

    elif random_index == 'paper' and response == 'scissors':
            #print(f'You win, since the computer picked {random_index}')
            print('You win, since the computer picked {} and you picked {}'.format(random_index,response))
            user +=1
    
    elif random_index == 'paper' and response == 'rocks':
            print(f'You lose, since the computer picked {random_index}')
            computer +=1

    elif random_index == 'rocks' and response == 'paper':
            print(f'You win, since the computer picked {random_index}')
            user +=1

    elif random_index == 'rocks' and response == 'scissors':
            print(f'You lose, since the computer picked {random_index}')
            computer +=1

    elif random_index == 'scissors' and response == 'rocks':
            print(f'You win, since the computer picked {random_index}')
            user +=1

    elif random_index == 'scissors' and response == 'paper':
            print(f'You Lose!, since the computer picked {random_index}')
            computer +=1

    print('\n')       
    if computer == 3 or user == 3:
        print(f'computer won {computer} games')
        print(f'you won {user} games')
        break
        
