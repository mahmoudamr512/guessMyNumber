#!/usr/bin/env python3

import random
import colorama

def numberValidator(playerNumber, randomNum):
    try:
        playerNumber = int(playerNumber)
        compareNums(playerNumber, randomNum)
    except:
        playerNumber = input(colorama.Fore.RED + 'Please make sure that you enter an integer: ')
        numberValidator(playerNumber, randomNum)

def compareNums(playerNumber, randomNum):
        if (playerNumber == randomNum):
            print(colorama.Fore.GREEN + "Good Job! You have guessed it correctly! The number was:" + str(randomNum))
            print(colorama.Fore.BLUE + "You won!")
        elif (playerNumber > randomNum):
            print(colorama.Fore.YELLOW + "Too high!")
            playerNumber = input(colorama.Fore.GREEN + 'Please enter the number again: ')
            numberValidator(playerNumber, randomNum)
        else:
            print(colorama.Fore.RED + "Too low!")
            playerNumber = input(colorama.Fore.GREEN + 'Please enter the number again: ')
            numberValidator(playerNumber, randomNum)



def main():
    randomNum = random.randint(1, 20)
    playerNumber = input(colorama.Fore.GREEN + 'Please enter your guess: ')
    numberValidator(playerNumber, randomNum)

if __name__ == "__main__": main()
