#!usr/bin/env python3

import random
import colorama


def compareNums(playerNumber, randomNum):
    if (playerNumber == randomNum):
        print(colorama.Fore.GREEN + "Good Job! You have guessed it correctly! The number was:" + str(randomNum))
        print(colorama.Fore.BLUE + "You won!")
    elif (playerNumber > randomNum):
        print(colorama.Fore.YELLOW + "Too high!")
        playerNumber = int(
            input(colorama.Fore.GREEN + 'Please enter the number again: '))
        compareNums(playerNumber, randomNum)
    else:
        print(colorama.Fore.RED + "Too low!")
        playerNumber = int(
            input(colorama.Fore.GREEN + 'Please enter the number again: '))
        compareNums(playerNumber, randomNum)

def main():
    randomNum = random.randint(1, 20)
    playerNumber = int(input(colorama.Fore.GREEN + 'Please enter your guess: '))
    compareNums(playerNumber, randomNum)

if __name__ == "__main__": main()
