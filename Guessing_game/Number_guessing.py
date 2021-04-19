"""
Number guessing
"""
from random import randint

def Is_int():
    dummy = input()
    if dummy == "Break":
        print('Bye Bye')
        return dummy
    else:
        try:
            dummy = int(dummy)
            return dummy
        except ValueError:
            print("That was not a number bro, try again: ")
            return Is_int()

def Guesser(min = 0, max = 10):
    print('Choose a min: ')
    min= Is_int()
    if type(min) == str:
        return None
    print('Choose a max: ')
    max = Is_int()
    if type(max) == str:
        return None
    number_to_guess = randint(min,max)
    print("Guess a number between " +str(min)+ " and "+str(max)+ " pls: ")
    guess = Is_int()
    while guess != number_to_guess and guess != 'Break':
        if guess > number_to_guess:
            print("Too high:  ")
            guess = Is_int()
        else:
            print('Too low: ')
            guess = Is_int()
    print("Oh yeah")

Guesser()
