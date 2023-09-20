import random
import sys
from termcolor import colored
import nltk
from nltk.corpus import words

nltk.download('words')


#function to create game board
def print_menu():
    print('Lets play Wordle:')
    print('Type a 5 letter word and hit enter!\n')
    print('-----\n')

    print('-----')
    print('-----')
    print('-----')
    print('-----')
    print('-----')
    print('-----')
    
    print('\033[F', end='')
    print('\033[F', end='')
    print('\033[F', end='')
    print('\033[F', end='')
    print('\033[F', end='')
    print('\033[F', end='')


#gather the set of all english words and create a list of all 5 letter words
word_list = words.words()
words_five = [word for word in word_list if len(word) == 5]


#if you would like to repeat the game
play_again = ""


while play_again != "q":
    print_menu()
    
    #Choose a random word from previously created list of only 5 letter words
    word = random.choice(words_five)

    #Provide 6 attempts
    for attempts in range(1, 7):
        while True:
            guess = input().lower()
            #Guesses must be a 5 letter word and also an existing english word
            if len(guess) == 5 and guess in words_five:

                #Else repeat
                break
            else:
                #Erase current line with ANSI terminal control sequence
                sys.stdout.write('\x1b[1A')
                sys.stdout.write('\x1b[2K')

        #Erase previous line from Python input function
        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')
 
        

        #Color letters to provide hints
        for i in range(5):
            if guess[i] == word[i]:
                print(colored(guess[i], 'green'), end="")
            elif guess[i] in word:
                print(colored(guess[i], 'yellow'), end="")
            else:
                print(guess[i], end="")

        print()


        #If guess was correct
        if guess == word:
            print(colored(f"Congrats! You got the wordle in {attempts}",
                          'red'))
            break

        #If attempts exceeds 6 guesses
        elif attempts == 6:
            print(f'Sorry the wordle was..{word}')
    play_again = input("Want to play again? Type q to exit.")
