#Create a program that ask 3 numbers (0-9) from the user.
#Generate 3 random winning numbers (0-9)
#Display “Winner” if all 3 input numbers matched the generated numbers
#Display ”You loss” if not
#Display ”Try again y/n” after each game
#If the user enter “y” the user will play again
#if “n” the program will exit.

import random
#Create an initial variable for random numbers and input nubers
List = []
random_List = ()
#Use while statement to loop the statements.
while List != random_List:
#Generate 3 random numbers and sort to place the numbers in order
    random_List = sorted(random.sample(range(0, 9), 3))
#Option: Check if the program will display winner if the random list and inputed list is equal
#    print(random_List)
#Ask 3 numbers for the user and sort to place the numbers in order
    number_One = int(input("Insert first number: "))
    number_Two = int(input("Insert second number: "))
    number_Three = int(input("Insert third number: "))
    Numbers = (number_One, number_Two, number_Three)
    List = sorted(Numbers)

#Compare the random number from inputed number
#if the random number is same in the inputed number diplay winner
    if List == random_List:
        print("Winner")
        break
#If the random number is different from the inputed number. display you lost
    if List != random_List:
        print("You Lost") 
#Create a menu that will ask if the user still want to continue or exit the game 
        print("Try again y/n")         
        try_Again = input()    
    if try_Again == "y":
        print("Try Again")
        continue
    elif try_Again == "n":
        print(f"You loss, the numbers are {random_List}")
        print("Exit")
        break