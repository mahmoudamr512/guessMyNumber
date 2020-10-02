import random
import colorama

randomNum = random.randint(1, 20)
playerNumber = int(input(colorama.Fore.GREEN + 'Please enter your guess: '))


def compareNums(playerNumber):
    if (playerNumber == randomNum):
        print(colorama.Fore.GREEN + "Good Job! You have guessed it correctly!")
        print(colorama.Fore.BLUE + "You won!")
    elif (playerNumber > randomNum):
        print(colorama.Fore.YELLOW + "Too high!")
        playerNumber = int(
            input(colorama.Fore.GREEN + 'Please enter the number again: '))
        compareNums(playerNumber)
    else:
        print(colorama.Fore.RED + "Too low!")
        playerNumber = int(
            input(colorama.Fore.GREEN + 'Please enter the number again: '))
        compareNums(playerNumber)


compareNums(playerNumber)
