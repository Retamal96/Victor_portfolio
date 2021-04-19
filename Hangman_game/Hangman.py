# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 20:02:02 2020

@author: victo
"""


def Hangman():
    import random
    
    word_list = ['tomate', 'aceitunas', 'domingo']
    word_to_guess = random.choice(word_list)
    return word_to_guess.upper()

def Create_frame(word_to_guess):    
    letter_list = list(word_to_guess)
    letter_tried = []
    word_tried = []
    guess = False
    tries = 6
    slas = []
    print("Let's play Hangman")
    print(display_hangman(tries))
    print("\n")
    for letter in range(len(word_to_guess)):
        slas.append('_')
    print(" ".join(slas))
    
    while guess == False and tries > 0:
        if slas == letter_list:
            guess == True
        
        else:
            Input_try = input("Try to guess: ").upper()   
            if Input_try.isalpha():
                if Input_try not in letter_tried and Input_try not in word_tried:               
                    for letter in range(len(letter_list)):
                        if  Input_try in letter_list[letter]:
                                slas[letter] = Input_try
                                       
                    if Input_try == word_to_guess:
                        print('Congratulations, {} was the word'.format(
                            word_to_guess.upper()))
                        slas = list(word_to_guess) 
                        guess = True               
                    elif Input_try in letter_list:
                        print('The letter {} was right'.format(Input_try))
                        letter_tried.append(Input_try)                    
                    elif Input_try not in letter_list:
                        letter_tried.append(Input_try)
                        tries = tries - 1
                        print('The letter {} was not right'.format(Input_try))
                        
                else:
                    print('you have already tried that')
                print(display_hangman(tries))
                print(" ".join(slas)) 
                if slas == letter_list:
                    print('You rock')
                    guess=True
            else:
                print('Incorrect input')
                
    if tries == 0:
        print(display_hangman(0))
        print('You are hang now')
def display_hangman(tries):
    stages = [  """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      
                   |
                   |
                   |
                   -
                   """
    ]
    return stages[tries]                         

def main():
    word = Hangman()
    Create_frame(word)
    while input("Wana play again? (Y/N) ").upper() == "Y":
        word = Hangman()
        Create_frame(word)
    
                
if __name__ == "__main__":
    main()
