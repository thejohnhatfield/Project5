# name: John Smith
# date: 06/20/2019
# description: Text-based space adventure game

import random
import time

def displayIntro():
    print("It is the end of a long year out in the vast galaxy of space")
    print("you come to crossroads on your trip home, one path leads home")
    print("where you will be rewarded for a job well done")
    print("and the other leads through a black hole that will end in your demise")
    print()

def choosePath():
    path = ""
    while path != "1" and path != "2": # input validation
        path = input("Which path will you choose? (1 or 2): ")

    return path

def checkPath(chosenPath):
    print("You head down the path")
    time.sleep(2)
    print("there's an asteroid nearby that looks familiar, that must be a good sign...")
    time.sleep(2)
    print("But your hairs on your arm begin to stand up...")
    print()
    time.sleep(2)

    correctPath = random.randint(1, 2)

    if chosenPath == str(correctPath):
        print("That sensation was just the feeling of admiration from the citizens of the galaxy!")
        print("Welcome home!")
    else:
        print("An extremely dark cloud begins to pull you in")
        print("causing all of the atoms in your body to dissociate")
        print("there is no trace left of your existence.")


playAgain = "yes"
while playAgain == "yes" or playAgain == "y":
    displayIntro()
    choice = choosePath()
    checkPath(choice) # choice is equal to "1" or "2"
    playAgain = input("Do you want to play again? (yes or y to continue playing): ")