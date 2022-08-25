# Simple python game to roll a dice

# import random to get random number
import random

# Role dice function
def rollDice():
    diceNumber = random.randint(1,6)
    print(diceNumber)

# End of function


# Roll again function
def rollAgain():
    end = 0
    while end == 0:
        play = int(input("\nEnter 1 to ROLL the dice and 2 to EXIT: "))
        if play == 1:
            rollDice()
        else:
            end = 1
            break
# End of function

rollAgain()