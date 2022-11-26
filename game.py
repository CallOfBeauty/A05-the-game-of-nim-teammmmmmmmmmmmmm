###################################################################
# Author: Dimitrios and Rodolfo
# Username: ntentiad, alvaradoreyesr2
#
# Assignment: A05: The Game of Nim
#
# Purpose: This program is designed to demonstrate the use of Python's string capabilities
# as a method for peeling digits from an integer
#
####################################################################################


import time
import random

def strategy(number):
    if number > 9:
        local=random.randrange(1,5)
        return local
    elif number<9 and number >5:
        local=number-5
        return local
    elif number==5:
        local = random.randrange(1, 5)
        return local
    else:
        return number






def main():
    numballs = 0
    humanremover = 5
    winner=""
    while numballs < 15:
        numballs = int(input("Please enter the number of balls, must be 15 or higher: "))
    while numballs > 0:
        while humanremover > 4:
            humanremover=int(input("How many balls do you wanna remove?"))
        numballs=numballs-humanremover
        humanremover = 5
        if numballs > 0:
            print("There are", numballs, "left")
            winner="computer"
        time.sleep(0.5)

        choice=strategy(numballs)

        numballs=numballs-choice
        if numballs > 0:
            print("The computer chose to remove: ", choice)
            print("There are", numballs, "left")
            winner="human"
        time.sleep(0.5)
    print(winner)
main()