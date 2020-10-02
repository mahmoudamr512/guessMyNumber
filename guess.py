import random

randomNum = random.randint(1,20)
playerNumber = int(input('Please enter your guess: '))

def compareNums(playerNumber):
    if (playerNumber == randomNum):
        print("Good Job! You have guessed it correctly!")
        print("You won!")
    elif (playerNumber > randomNum):
        print("Too high!")
        playerNumber = int(input('Please enter the number again: '))
        compareNums(playerNumber)
    else:
        print("Too low!")
        playerNumber = int(input('Please enter the number again: '))
        compareNums(playerNumber)

compareNums(playerNumber)